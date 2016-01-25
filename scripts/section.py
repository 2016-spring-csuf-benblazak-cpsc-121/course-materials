#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <benblazak.dev@gmail.com>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# Project located at <https://github.com/benblazak/text-processing-utilities>
# -----------------------------------------------------------------------------

'''A script/module to 'section' files -- that is, to take one file and produce
some number of others, where each of the derivative files contains some subset
of the lines in the original.

If run as a script, `input` is called with the arguments passed via the command
line (except for the program name).

The basic syntax for input files is
```
normal text normal text
// SECTION BEGIN section-name
this text will be included in the 'section-name' section
// SECTION END section-name
normal text normal text
```
'''

# -----------------------------------------------------------------------------

import os.path
import re
import sys
import textwrap

# -----------------------------------------------------------------------------

class Section:

    class Error(Exception):
        pass

    class SyntaxError(Exception):
        pass

    def raiseSyntaxError(self, message):
        raise self.SyntaxError(
            '"' + self._filename + '"'
            + ' line '
            + str( self._lineno )
            + ': '
            + message
        )

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    def __init__(self):

        # (managed by `self.input`)
        self._filename = None  # the name of the current file

        # (managed by `self.section`)
        self._lineno = None  # the current line number

        # (used by `self.section`)
        self._esc = '//'  # the string beginning a section command

    # .........................................................................

    def section(self):
        '''Break `self._filename` into sections.
        '''

        section_re = self._esc + r'\s*SECTION'
        ignore_re  = r'\s+IGNORE'  # ignore line
        begin_re   = r'\s+BEGIN'
        end_re     = r'\s+END'
        pause_re   = r'\s+PAUSE'
        resume_re  = r'\s+RESUME'
        indent_re  = r'\s+INDENT'  # reset indent
        name_re    = r'\s+([\w-]+)'

        section = re.compile( section_re )
        ignore  = re.compile( section_re + ignore_re )
        begin   = re.compile( section_re + begin_re + name_re )
        end     = re.compile( section_re + end_re + name_re )
        pause   = re.compile( section_re + pause_re + name_re )
        resume  = re.compile( section_re + resume_re + name_re )
        indent  = re.compile( section_re + indent_re + name_re )

        sections_lines  = { 'all':'' }  # the lines of text, for every section
        sections_open   = { 'all' }     # sections currently being processed
        sections_indent = { 'all':0 }   # number of initial chars to discard

        f = open(self._filename)

        self._lineno = 0;
        for line in f:
            self._lineno += 1
            if ignore.search(line):
                pass
            elif begin.search(line):
                name = begin.search(line).group(1)
                sections_lines[name] = ''
                sections_open.add(name)
                sections_indent[name] = re.search( r'\S', line ).start()
            elif end.search(line):
                name = end.search(line).group(1)
                if name in sections_open:
                    sections_open.remove(name)
                else:
                    raiseSyntaxError( 'Illegal SECTION in input file' )
            elif pause.search(line):
                name = pause.search(line).group(1)
                if name in sections_open:
                    sections_open.remove(name)
                else:
                    raiseSyntaxError( 'Illegal SECTION in input file' )
            elif resume.search(line):
                name = resume.search(line).group(1)
                sections_open.add(name)
            elif indent.search(line):
                name = indent.search(line).group(1)
                sections_indent[name] = re.search( r'\S', line ).start()
            else:
                if section.search(line):
                    raiseSyntaxError( 'Illegal SECTION in input file' )
                for name in sections_open:
                    sections_lines[name] += line[sections_indent[name]:] or '\n'

        return sections_lines

    def input(self, *args):
        '''Handle command line arguments.
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
            'usage: ' + sys.argv[0] + ' [OPTIONS] INPUT_FILE',
            '',
            wrap( width=79, indent=0, text='''
                Options may be placed anywhere in the list of arguments.
            ''' ),
            '',
            '-h|--help', wrap( width=79-4, indent=4, text='''
                Show this documentation and exit.
            ''' ),
            '',
            '-l|--list', wrap( width=79-4, indent=4, text='''
                Show the section names contained in the input file as a comma
                separated list, and exit.
            ''' ),
            '',
            '-e|--escape ESC', wrap( width=79-4, indent=4, text='''
                Set the "escape sequence", i.e. the string that begins a
                section command in INPUT_FILE.  By default, this value is set
                based on the filename extension (or '//' if the extension is
                not known).  Later occurrences of this option override earlier
            ones.
            ''' ),
            '',
            '-b|--base BASE', wrap( width=79-4, indent=4, text='''
                See [-o | --output].  By default, BASE is set to INPUT_FILE.
                Later occurrences of this option override earlier ones.
            ''' ),
            '',
            '-o|--output SECTIONS', wrap( width=79-4, indent=4, text='''
                Write each NAME in SECTIONS (where SECTIONS is a comma
                separated list of section names) to BASE.section.NAME.  By
                default, all possible sections are written.  Later occurrences
                of this option override earlier ones.
            ''' ),
        ))

        # vars
        self._filename = None
        _list = None
        base = None
        output = None

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

            elif arg in ( '-l', '--list' ):
                _list = True

            elif arg in ( '-e', '--escape' ):
                try:
                    self._esc = next(it)
                except StopIteration:
                    error( '[-e | --escape] requires a following argument' )

            elif arg in ( '-b', '--base' ):
                try:
                    base = next(it)
                except StopIteration:
                    error( '[-b | --base] requires a following argument' )

            elif arg in ( '-o', '--output' ):
                try:
                    output = [ s.strip() for s in next(it).split(',') ]
                except StopIteration:
                    error( '[-o | --output] requires a following argument' )

            else:
                if self._filename is None:
                    self._filename = arg
                else:
                    error( 'Multiple INPUT_FILEs given' )

        # error check
        if self._filename is None:
            error( 'No INPUT_FILE given' )

        # set defaults
        if self._filename.endswith('.py'): self._esc = '#'
        if self._filename.endswith('.tex'): self._esc = '%'
        if self._esc is None: self._esc = '//'

        if _list is None: _list = False
        if base is None: base = self._filename

        # section

        sections = self.section()

        if _list is True:
            print(','.join(sections.keys()))
            return

        for s,lines in sections.items():
            if output is None or s in output:
                with open(base + '.section.' + s, 'w') as f:
                    f.write(lines)

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    Section().input( *sys.argv[1:] )

