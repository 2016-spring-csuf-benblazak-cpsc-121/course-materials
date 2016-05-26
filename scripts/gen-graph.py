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

del sys.path[0]

# -----------------------------------------------------------------------------

assigned = [
    g['predictions']['current grade'] for g in grades.grades.values()
]
letters = [
    grades.letter(round(p*100,2)).lower() if isinstance(p, float) else p.lower() for p in assigned
]

counts = dict()
for g in letters:
    if g not in counts:
        counts[g] = 0
    counts[g] += 1

pass_  = 0
fail_  = 0
other_ = 0
for l in 'a', 'b', 'c':
    for pm in '+', '', '-':
        if l+pm in counts:
            pass_ += counts[l+pm]
for l in 'd', 'f':
    for pm in '+', '', '-':
        if l+pm in counts:
            fail_ += counts[l+pm]
for l in 'w':
    for pm in '+', '', '-':
        if l+pm in counts:
            other_ += counts[l+pm]

# .............................................................................

for l in 'a', 'b', 'c', 'd', 'f', 'w':
    for pm in '+', '', '-':
        if l+pm not in counts:
            continue
        print( l+pm + ' ' * (4-len(l+pm)) + '*' * counts[l+pm] )

print()

for l in 'a', 'b', 'c', 'd', 'f', 'w':
    print( l + ' ' + '*' * sum([ counts.get(l+pm, 0) for pm in ('+', '', '-') ]) )

print()

print(
    'pass  ' + '*' * pass_ + '\n' +
    'fail  ' + '*' * fail_ + '\n' +
    'other ' + '*' * other_ + '\n'
)

