#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <benblazak.dev@gmail.com>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

'''A script/module implementing a simple preprocessor for text files.

If run as a script, `input` is called with the arguments passed via the command
line (except for the program name, and with '-o -' prepended).

The basic syntax for input files is
```
normal text normal text !function_1,function_2(this text will be passed to
self.function_2 as a string; the result will be passed to self.function_1 as a
string; and the result of that will be output in place of this 'escape block')
normal text normal text
```
where the functions may in general do whatever they want (i.e. whatever python3
is capable of doing).


References:
- about iterators and generators:
  <http://chimera.labs.oreilly.com/books/1230000000393/ch04.html>
- about exec and eval (mostly in python 2):
  <http://lucumr.pocoo.org/2011/2/1/exec-in-python/>
'''

# -----------------------------------------------------------------------------

import functools
import os.path
import re
import sys
import textwrap

# open `sys.stdin` and `sys.stdout` with universal newlines
sys.stdin = open( sys.stdin.fileno() )
sys.stdout = open( sys.stdout.fileno(), 'w' )

# -----------------------------------------------------------------------------

class Namespace:
    pass

# -----------------------------------------------------------------------------

class Prep:

    class Error(Exception):
        pass

    class SyntaxError(Error):
        pass

    def raiseError(self, message):
        raise self.Error(
            '"' + self._filename + '"'
            + ' line '
            + str( self._in.count('\n', 0, self._pos) + 1 )
            + ': '
            + message
        )

    def raiseSyntaxError(self, message):
        raise self.SyntaxError(
            '"' + self._filename + '"'
            + ' line '
            + str( self._in.count('\n', 0, self._pos) + 1 )
            + ': '
            + message
        )

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    def __init__(self):

        # (managed by `self.input`)
        self._jobname = None   # as in LaTeX
        self._filename = None  # the name of the current file, or ''

        # (managed by `self.prep`)
        self._in = None   # the input string
        self._pos = None  # the current position in `self._in`
        self._out = None  # the list of strings to ''.join() into the output

        # (used by `self.prep`)
        self._esc = '!'  # the string beginning an "escape"

        # (used by `self.indent`)
        self._indent = 4  # the default number of spaces to indent

    # (managed by `self.input`)

    @property
    def _path(self):
        return sys.path

    @_path.setter
    def _path(self, p):
        sys.path = p

    # .........................................................................

    class Global:
        '''Provide access (more or less) to the global namespace via `self`.

        WARNINGS:
        - In general, this should only be used to call functions that take a
          string and return some printable object.  Functions that have side
          effects, especially the global versions of `eval` and `exec`, should
          be avoided, or used very very carefully.
        '''
        def __getattr__(self, key):
            '''Search for the given attribute in the module namespace, then in
            the builtins dictionary.
            '''
            for module in ( sys.modules[__name__], globals()['__builtins__'] ):
                try:
                    return getattr( module, key )
                except AttributeError:
                    pass

            raise AttributeError(
                str(type(self)) + ': could not find ' + "'" + key + "'"
            )
    Global = Global()

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    def eval(self, _in):
        '''`eval` the given text and return the result.
        '''
        return eval(self.dedent(_in))

    def exec(self, _in):
        '''`exec` the given text inside a function.

        It's useful to wrap the given text in a function then call that
        function inside the `exec`, rather than just `exec`ing it directly,
        because of the way python3 handles local variables inside an `exec`.
        '''
        exec('\n'.join([
            'def function(self, _in):',
            self.indent(self.dedent(_in)),
            'function(self, _in)',
        ]))

    def geval(self, _in):
        '''`eval` the given text in the global namespace and return the result.
        '''
        return eval(self.dedent(_in), globals())

    def gexec(self, _in):
        '''`exec` the given text in the global namespace.
        '''
        exec(self.dedent(_in), globals());

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    def comment(self, _in):
        '''Ignore given text.
        '''
        pass

    def comment_to_newline(self, _in):
        '''Delete preceding whitespace up to a newline (exclusive), and
        following text up to a newline (exclusive).
        '''
        pos = self._out[-1].rfind('\n')
        pos = re.compile( r'\s*$' ).search( self._out[-1], pos+1 ).start()
        self._out[-1] = self._out[-1][:pos]

        pos = self._in.find('\n', self._pos)
        if pos == -1: self._pos = len(self._in)
        else:         self._pos = pos

    def delete_to_newline(self, _in):
        '''Delete following text up to the following newline (inclusive).
        '''
        pos = self._in.find('\n', self._pos)
        if pos == -1: self._pos = len(self._in)
        else:         self._pos = pos+1

    def delete_whitespace(self, _in):
        '''Delete preceding and following whitespace.

        Notes:
        - Preceding data has already been processed.
        - Following data has not net been processed.
        '''
        self.delete_whitespace_left(_in)
        self.delete_whitespace_right(_in)

    def delete_whitespace_left(self, _in):
        '''Delete preceding whitespace.

        Notes:
        - Acts on data that has already been processed.
        '''
        self._out[-1] = self._out[-1].rstrip()

    def delete_whitespace_right(self, _in):
        '''Delete following whitespace.

        Notes:
        - Acts on data that has not yet been processed.
        '''
        self._pos = re.compile( r'\s*' ).match( self._in, self._pos ).end()

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    def print(self, *args, sep=' ', end=''):
        '''Add the given text to `self._out`.

        Notes:
        - It probably wouldn't make much sense to put this function in a
          function list; but it might be useful inside an exec, for instance :)
        '''
        self._out.append( sep.join([str(o) for o in args]) + end )

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    def repr(self, _in):
        r'''Returns a string containing a printable representation of an
        object.

        Good for quoting within an eval or exec, similar to a raw triple quoted
        string, as in
        ```
        !exec,prep(
            for i in range(0,5):
                self.print( !repr,strip,dedent(
                  repeated text!
                ), end='\n' )
        )!delete_to_newline
        ```
        '''
        return repr(_in)

    def strip(self, _in):
        '''Remove leading and trailing whitespace in the given text.
        '''
        return _in.strip()

    def dedent(self, _in):
        '''Remove common leading whitespace in the given text.
        '''
        return textwrap.dedent(_in)

    def indent(self, _in, level=None):
        '''Indent the given text by `level` spaces.
        '''
        if level is None: level = self._indent
        return textwrap.indent( _in, ' '*level )
    indent_1 = lambda self, _in: self.indent(_in, level=1)
    indent_2 = lambda self, _in: self.indent(_in, level=2)
    indent_3 = lambda self, _in: self.indent(_in, level=3)
    indent_4 = lambda self, _in: self.indent(_in, level=4)
    indent_5 = lambda self, _in: self.indent(_in, level=5)
    indent_6 = lambda self, _in: self.indent(_in, level=6)
    indent_7 = lambda self, _in: self.indent(_in, level=7)
    indent_8 = lambda self, _in: self.indent(_in, level=8)

    # .........................................................................

    def prep(self, _in):
        '''Preprocess the given input string.
        '''

        old = ( self._in, self._pos, self._out )
        ( self._in, self._pos, self._out ) = ( _in, 0, [] )


        while True:
            match = re.compile(
                r'(' + re.escape(self._esc) + r')([\w.,]*)(\(*)'
            ).search( self._in, self._pos )

            if match is None:
                self._out.append(self._in[self._pos:])
                break

            # - this will always append at least an empty string, so
            #   `self._out` will not be empty when the first function is called
            #   below
            self._out.append(self._in[self._pos:match.start()])
            self._pos = match.end()

            if match.group(2) == '' and match.group(3) == '':
                self._out.append(match.group())
                continue

            # save the pieces of `match` that we need (it may change below)
            functions = match.group(2)
            left = match.group(3)
            right = ')' * len(left)

            if len(left) > 0:
                delimiter = re.compile(
                    r'(' + re.escape(left) + r')|(' + re.escape(right) + r')'
                )
                count = 1
                while count > 0:
                    match = delimiter.search( self._in, match.end() )
                    if match is None:
                        self.raiseSyntaxError( 'Unbalanced delimiter' )
                    if match.group(1) is not None:
                        count += 1
                    else:
                        count -= 1

            start_pos = self._pos  # in case there's an error
            substring = self._in[self._pos:match.start()]
            self._pos = match.end()
            for function in reversed(functions.split(',')):
                try:
                    function = \
                        functools.reduce(getattr, [self]+function.split('.'))
                    substring = function(substring)
                    substring = str(substring) if substring is not None else ''
                except Exception:
                    self._pos = start_pos
                    self.raiseError( '`prep` failed' )
            self._out.append(substring)

        _out = ''.join(self._out)
        ( self._in, self._pos, self._out ) = old
        return _out

    # .........................................................................

    def input(self, *args):
        '''Read and preprocess files and/or `sys.stdin`.

        When called within a .prep file, this function behaves as described by
        `usage`, except that
        - If there is no [-o | --output], the result of running `self.prep` on
          the input will be returned as a string
        - If `self._jobname` is not `None` (which it always will be, when
          called from the command line) and there is no [--jobname],
          `self._jobname` will not be changed

        When called via the command line, this function behaves as described by
        `usage`.

        Notes:
        - I'm not using `argparse` for this because loading it seems to take a
          small, but noticeable, amount of time (about 0.015 seconds).
        '''

        def wrap(width, indent, text):
            return '\n'.join(
                textwrap.wrap(
                    textwrap.dedent( text ).lstrip(),
                    width = width,
                    initial_indent = ' ' * indent,
                    subsequent_indent = ' ' * indent,
                )
            )
        usage = '\n'.join((
            'usage: ' + sys.argv[0] + ' [OPTIONS] INPUT_FILE*',
            '',
            wrap( width=79, indent=0, text='''
                Options may be placed anywhere in the list of arguments.  If no
                INPUT_FILE is present, input will be read from stdin.
            ''' ),
            '',
            '-h|--help', wrap( width=79-4, indent=4, text='''
                Show this documentation and exit.
            ''' ),
            '',
            '-o|--output FILE', wrap( width=79-4, indent=4, text='''
                If FILE is -, write to stdout (this is the default).  Otherwise
                write to FILE.  Later occurrences of this option override
                earlier ones.
            ''' ),
            '',
            '--jobname NAME', wrap( width=79-4, indent=4, text='''
                Set the name of this job (by default the basename of the first
                input file, or '' if the first input is stdin).  Later
                occurrences of this option override earlier ones.
            ''' ),
            '',
            '--', wrap( width=79-4, indent=4, text='''
                Process all remaining arguments as input files (this may be
                useful if some filenames begin with -).
            ''' ),
        ))

        # vars
        inputs = []
        output = None
        jobname = None

        # helper functions
        def error(message):
            print( sys.argv[0]+':', message, file=sys.stderr )
            print( usage, file=sys.stderr )
            exit(1)

        # process arguments
        it = iter(args)
        for arg in it:

            if arg in ( '-h', '--help' ):
                print(usage)
                exit(0)

            elif arg in ( '-o', '--output' ):
                try:
                    output = next(it)
                except StopIteration:
                    error( '[-o | --output] requires a following argument' )

            elif arg in ( '--jobname', ):
                try:
                    jobname = next(it)
                except StopIteration:
                    error( '[--jobname] requires a following argument' )

            elif arg == '--':
                for arg in it:
                    inputs.append(open(arg))

            elif arg == '-':
                inputs.append(sys.stdin)

            elif arg[0] == '-':
                error( 'unknown option: ' + arg )

            else:
                inputs.append(open(arg))

        # normalize
        if inputs == []:
            inputs.append(sys.stdin)

        if output is not None:
            if output == '-':
                output = sys.stdout
            else:
                output = open(output, 'w')

        # prep

        old = ( self._jobname, self._filename, self._path )
        _out = []

        if jobname is not None:
            self._jobname = jobname
        elif self._jobname is None:
            if isinstance(inputs[0].name, str):
                self._jobname = \
                    os.path.basename(os.path.normpath(inputs[0].name))
            else:
                self._jobname = ''
                # - `sys.stdin.name` will not be a string, because we reopened
                #   it by file descriptor at the top of the module

        for i in inputs:
            self._path = old[-1].copy()  # each input has its own sys.path

            if i == sys.stdin:
                self._filename = ''
                self._path[0] = ''
            else:
                self._filename = os.path.normpath(i.name)
                self._path[0] = os.path.dirname(os.path.abspath(i.name))

            _out += self.prep(i.read())

        _out = ''.join(_out)
        ( self._jobname, self._filename, self._path ) = old

        # return
        if output is not None:
            print( _out, end='', file=output )
        else:
            return _out

# -----------------------------------------------------------------------------

setattr( Prep, 'g', Prep.Global )

setattr( Prep, '', Prep.eval )
setattr( Prep, 'c', Prep.comment )

setattr( Prep, 'cnl', Prep.comment_to_newline )
setattr( Prep, 'dnl', Prep.delete_to_newline )
setattr( Prep, 'dws', Prep.delete_whitespace )
setattr( Prep, 'dwsl', Prep.delete_whitespace_left )
setattr( Prep, 'dwsr', Prep.delete_whitespace_right )

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    Prep().input( '-o', '-', *sys.argv[1:] )

