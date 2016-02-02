#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import collections
import os
import os.path

import github3

import common
import standards
import students

# -----------------------------------------------------------------------------

class Error(Exception):
    pass

# -----------------------------------------------------------------------------

def _gen_grades():
    org = '2016-spring-csuf-benblazak-cpsc-121'

    if common.DEBUG: studentdir = './test/students'
    else:            studentdir = '../../../students'

    scandir = os.path.join(studentdir, 'scans')

    # .........................................................................

    name2cwid = {
        v['github'].lower():k
        for k,v in students.students.items()
        if 'github' in v
    }

    grades = {
        cwid: collections.OrderedDict((
            ((g,s,),collections.OrderedDict())
            for g,ss in standards.groups.items()
            for s in ss
        ))
        for cwid in students.students
    }

    # .........................................................................

    # TODO: write this out to a file, in case we can't get it from github (and
    # fall back to that)

    github = github3.GitHub()

    for r in github.iter_user_repos(org):
        r = r.name
        if r in ( 'course-materials', ): continue
        assignment = 'a' + r[-2:]

        for cwid in students.students:
            grades[cwid][('assignment completion', '')][assignment] = None

        for pr in github.iter_repo_issues(org, r, state='all'):
            name = pr.user.login
            if name not in name2cwid: continue

            grades[name2cwid[name]] \
                  [('assignment completion', '')] \
                  [assignment] = 4

        import pprint
        pprint.pprint(grades)
        exit(0)

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

