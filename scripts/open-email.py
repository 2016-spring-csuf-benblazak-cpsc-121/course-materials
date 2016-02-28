#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <benblazak.dev@gmail.com>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# Project located at <https://github.com/benblazak/text-processing-utilities>
# -----------------------------------------------------------------------------

"""A script to print out some subset of student names and emails, in a format
suitable for the `openEmail` function in `open-email.applescript`.
"""

import os
import os.path
import subprocess
import sys
import textwrap
import time

import common

filedir = os.path.dirname(os.path.abspath(__file__))

students = common.importfile( os.path.join(filedir, '../students.py') )

# -----------------------------------------------------------------------------

if len(sys.argv) == 1:
    arg = 'all'
elif len(sys.argv) == 2:
    arg = sys.argv[1]
else:
    print('ERROR: too many arguments')
    sys.exit(1)

# .............................................................................

cwids = []

if arg == 'all':
    cwids = students.students.keys()

elif arg == 'no-github':
    cwids = [ cwid for cwid in students.students
              if 'github' not in students.students[cwid] ]

elif arg.startswith('section-'):
    cwids = [ cwid for cwid,info in students.students.items()
              if 'section' in info
              and info['section'] in arg[8:].split(',') ]

else:
    print('ERROR: unrecognized argument')
    sys.exit(1)

# .............................................................................

_from = 'Ben Blazak <bblazak@fullerton.edu>'
_to = ',\n '.join([
    info['alias'] + ' <' + info['email'] + '>'
    for cwid,info in students.students.items()
    if cwid in cwids
    and 'alias' in info
    and 'email' in info
])

boundary = 'CONTENTBOUNDARY'

email = ''

email += textwrap.dedent('''\
    From: {_from}
    Bcc: {_to}
    Subject: [CPSC 121]
    Content-Type: multipart/mixed; boundary={boundary}

    To view this message properly, please use a MIME enabled client.

    --{boundary}
    Content-Type: text/plain
    Content-Transfer-Encoding: quoted-printable

    Dear students,



    Sincerely,
    Ben Blazak
    --{boundary}--
''').format(**locals())

# .............................................................................

tempfile = os.path.abspath(os.path.join(
    filedir, 'open-email--temp.eml'
))

with open(tempfile, 'w') as f:
    f.write(email)

time.sleep(1)

script = textwrap.dedent('''
    open "{tempfile}"
    osascript <<END
    tell application "Mail" to activate
    delay 1
    tell application "System Events" to ¬
        keystroke "d" using {{command down, shift down}}
    END
''').format(**locals())

sp = subprocess.Popen( script, shell = True )
sp.communicate()

os.remove(tempfile)

