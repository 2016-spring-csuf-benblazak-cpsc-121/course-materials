#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import os
import os.path
import sys

# .............................................................................

filedir = os.path.dirname(os.path.abspath(__file__))
os.chdir(filedir)

sys.path.insert(1, '..')

import grades
import students

del sys.path[0]

# -----------------------------------------------------------------------------

sections = [ s['section'] if 'section' in s else None
             for s in students.students.values() ]
sections = [ s for s in sections if s is not None ]
sections = set(sections)

for section in sections:
    values = [ v for k,v in grades.grades.items()
               if 'si' not in k
               and 'section' in students.students[k]
               and students.students[k]['section'] == section ]

    cmnt = [ g[('design','documentation')]['overall'] for g in values ]
    code = [ g[('review','functions')]['overall'] for g in values ]
    oop  = [ g[('object-oriented programming','classes')]['overall'] for g in values ]

    print( '-------', 'cpsc 121-' + section, '-------' )

    for i in 'cmnt', 'code', 'oop':
        print(i)
        scores = globals()[i]
        print( '    sat', len([ s for s in scores if s is not None and s >= 3.5 ]) )
        print( '    dev', len([ s for s in scores if s is not None and s == 3 ]) )
        print( '  unsat', len([ s for s in scores if s is None or s <= 2 ]) )
        print( '  total', len(scores) )
        print()

