#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import os.path

import common

# -----------------------------------------------------------------------------

filedir = os.path.dirname(os.path.abspath(__file__))

_students = common.importfile(os.path.join(filedir, '../../students.py'))

_github2cwid = {
    v['github'].lower():k
    for k,v in _students.students.items()
    if 'github' in v
}

# -----------------------------------------------------------------------------

grades = {
    _students.lookup('o s'): { 'extra credit': 1 },
    _students.lookup('f s'): { 'overall': 'I' },
    _students.lookup('o s'): { 'overall': 0.98 },
    _students.lookup('tw s'): { 'overall': 0.82 },
}

