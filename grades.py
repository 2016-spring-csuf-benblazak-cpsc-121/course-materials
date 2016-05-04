#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import os
import os.path
import requests
import sys
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
        cwid: OrderedDict( [
            ('extra credit', 0),
            ('overall', None),
            ('predictions', OrderedDict()),
        ] + [
            ((g,s,),OrderedDict())
            for g,ss in standards.groups.items()
            for s in ss
        ] )
        for cwid in students.students
    }

    # .........................................................................
    # from github

    github = github3.GitHub()

    try:
        for r in sorted([ r.name for r in github.iter_user_repos(common.org) ]):
            if r in ( 'course-materials', ): continue
            assignment = 'a' + r[-2:]

            for cwid in students.students:
                grades[cwid][('assignment completion', '')][assignment] = None

            for pr in github.iter_repo_issues(common.org, r, state='all'):
                name = pr.user.login.lower()
                if name not in name2cwid: continue

                grades[name2cwid[name]] \
                      [('assignment completion', '')] \
                      [assignment] = True

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
    # from scans
    
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
            if f.startswith('_'): continue

            (i.name, i.scores) = \
                f.split('.',maxsplit=1)[0].split(',', maxsplit=1)
            if len(i.scores) != len(i.standards):
                raise Error(
                    'WARNING: mismatch in number of scores for'
                    + ' "' + os.path.join(d, f) + '"' )

            i.scores = [
                None if s == 'x' else
                3.5 if s == '5' else
                3.75 if s == '7' else
                int(s)
                for s in i.scores
            ]

            for sta,sco in zip(i.standards,i.scores):
                try:
                    grades[students.lookup(i.name)][sta][i.assessment] = sco
                except students.Error:
                    raise Error(
                        'Name lookup failed for '
                        + ' "' + os.path.join(d, f) + '"' )

    # .........................................................................
    # from file

    private = common.importfile(os.path.join(studentdir, 'grades.py'))

    for cwid in private.grades:
        if cwid in grades: grades[cwid].update(private.grades[cwid])
        else:              grades[cwid] = private.grades[cwid]

    # .........................................................................

    for cwid in grades:
        overall = 0
        maximum = 0

        for sta,assessments in grades[cwid].items():
            if isinstance(sta, str): continue

            scos = [ sco for sco in assessments.values() if sco is not None ]

            if sta == ('assignment completion', ''):
                sco = len(scos)/len(assessments) if len(assessments) > 0 else 0
                assessments['overall'] = sco
                overall += sco * standards.multipliers[sta]
                maximum += standards.multipliers[sta]
                continue

            if len(scos) == 0:
                assessments['overall'] = None

            else:
                if len(scos) == 1 or scos[-1] >= scos[-2]:
                    sco = scos[-1]

                else:  # scos[-1] < scos[-2]
                    sco = [ sco for sco in [1, 2, 3, 3.5, 3.75, 4]
                            if (scos[-1]+scos[-2])/2 <= sco ][0]

                assessments['overall'] = sco
                if sco >= 3:
                    overall += sco / 4 * standards.multipliers[sta]
                maximum += standards.multipliers[sta]

        ec = grades[cwid]['extra credit'] * 0.002

        if grades[cwid]['overall'] is None:
            grades[cwid]['overall'] = overall + ec

        grades[cwid]['predictions']['current grade'] = grades[cwid]['overall']
        if maximum == 0:
            grades[cwid]['predictions']['average'] = None
            grades[cwid]['predictions']['maximum without reassessing'] = None
        else:
            grades[cwid]['predictions']['average'] = overall / maximum
            grades[cwid]['predictions']['maximum without reassessing'] = \
                1 - maximum + overall + ec

    # .........................................................................

    return grades

# -----------------------------------------------------------------------------

grades = _gen_grades()

# -----------------------------------------------------------------------------

# SECTION BEGIN letter
def letter(percent):
    if   percent >= 97: return 'A+'
    elif percent >= 93: return 'A'
    elif percent >= 90: return 'A-'
    elif percent >= 87: return 'B+'
    elif percent >= 83: return 'B'
    elif percent >= 80: return 'B-'
    elif percent >= 77: return 'C+'
    elif percent >= 70: return 'C'
    elif percent >= 50: return 'D'
    else              : return 'F'
# SECTION END letter

