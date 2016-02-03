#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import os
import os.path
import requests
from collections import OrderedDict

import github3

import common
import standards
import students

# -----------------------------------------------------------------------------

class Error(Exception):
    pass

class Namespace():
    pass

# -----------------------------------------------------------------------------

def _gen_grades():
    org = '2016-spring-csuf-benblazak-cpsc-121'

    filedir = os.path.dirname(os.path.abspath(__file__))

    if common.DEBUG: studentdir = './test/students'
    else:            studentdir = '../../../students'
    studentdir = os.path.abspath(os.path.join(filedir, studentdir))

    assignmentsfile = os.path.join(studentdir, 'assignments.gen.py')
    scandir = os.path.join(studentdir, 'scans')

    # .........................................................................

    name2cwid = {
        v['github'].lower():k
        for k,v in students.students.items()
        if 'github' in v
    }

    grades = {
        cwid: OrderedDict( [ ('extra credit', 0) ] + [
            ((g,s,),OrderedDict())
            for g,ss in standards.groups.items()
            for s in ss
        ])
        for cwid in students.students
    }

    # .........................................................................

    github = github3.GitHub()

    try:
        for r in sorted([ r.name for r in github.iter_user_repos(org) ]):
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

        with open(assignmentsfile, 'w') as f:
            f.write(repr({
                cwid: grades[cwid][('assignment completion', '')]
                for cwid in grades
            }))

    except (requests.exceptions.ConnectionError, github3.models.GitHubError):
        assignments = eval(open(assignmentsfile).read())
        none = OrderedDict([
            (a, None) for a in assignments[list(assignments.keys())[0]]
        ])
        for cwid in grades:
            if cwid in assignments:
                grades[cwid][('assignment completion', '')] = assignments[cwid]
            else:
                grades[cwid][('assignment completion', '')] = none

    # .........................................................................
    
    for d in sorted(os.listdir(scandir)):
        if d.startswith('.'): continue

        i = Namespace()

        (i.date, i.assessment, i.standards) = d.split(',', maxsplit=2)
        i.standards = [ standards.lookup(s) for s in i.standards.split(',') ]

        for cwid in students.students:
            for sta in i.standards:
                grades[cwid][sta][i.assessment] = None

        for f in os.listdir(os.path.join(scandir, d)):
            if f.startswith('.'): continue

            (i.name, i.scores) = \
                f.split('.',maxsplit=1)[0].split(',', maxsplit=1)
            i.scores = [
                None if s == '' else
                3.5 if s == '5' else
                3.75 if s == '7' else
                int(s)
                for s in i.scores.split(',')
            ]

            for sta,sco in zip(i.standards,i.scores):
                grades[students.lookup(i.name)][sta][i.assessment] = sco

    # .........................................................................

    # TODO: calculate overall grades

    # .........................................................................

    # TODO: update grades from other file

    # .........................................................................

    return grades

# -----------------------------------------------------------------------------

grades = _gen_grades()

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

