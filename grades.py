#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import os
import os.path

import common
import standards
import students

# -----------------------------------------------------------------------------

class Error(Exception):
    pass

# -----------------------------------------------------------------------------


# TODO: not sure if this is how we want to do things
def _gen_grades():
    if common.DEBUG: studentdir = './test/students'
    else:            studentdir = '../../../students'

    scandir = os.path.join(studentdir, 'scans')

    # .........................................................................

    # TODO: pull assignments from github

    # .........................................................................
    
    # TODO: pull grades from scans

    for d in os.listdir(scandir):
        if d.startswith('.'): continue

        for f in os.listdir(os.path.join(scandir, d)):
            if f.startswith('.'): continue

            print(d, f)

_gen_grades()

# -----------------------------------------------------------------------------

# SECTION BEGIN letter
def letter(percent):
    if   percent >= 97: return 'A+'
    elif percent >= 93: return 'A'
    elif percent >= 90: return 'A-;'
    elif percent >= 87: return 'B+'
    elif percent >= 83: return 'B'
    elif percent >= 80: return 'B-;'
    elif percent >= 77: return 'C+'
    elif percent >= 70: return 'C'
    elif percent >= 50: return 'D'
    else              : return 'F'
# SECTION END letter

