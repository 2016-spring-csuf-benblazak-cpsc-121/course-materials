#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <benblazak.dev@gmail.com>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# Project located at <https://github.com/benblazak/text-processing-utilities>
# -----------------------------------------------------------------------------

"""A script to print out some subset of student names and emails, in a format
suitable for the `openEmail` function in `open-email.applescript`.
"""

import os.path
import sys

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

vs = students.students.values()

if arg == 'all':
    pass

elif arg == 'no-github':
    vs = [ v for v in vs if 'github' not in v ]

elif arg.startswith('section-'):
    vs = [ v for v in vs
           if 'section' in v and v['section'] in arg[8:].split(',') ]

else:
    print('ERROR: unrecognized argument')
    sys.exit(1)

# .............................................................................

print(
    '{ ' + ', '.join([
        '{name: "' + v['alias'] + '", email: "' + v['email'] + '"}'
        for v in vs if 'alias' in v and 'email' in v
    ]) + ' }'
)

