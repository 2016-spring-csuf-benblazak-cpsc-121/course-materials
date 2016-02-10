#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import os
import os.path
import re
import sys

import common

# -----------------------------------------------------------------------------

class Error(Exception):
    pass

# -----------------------------------------------------------------------------

def _gen_students():

    filedir = os.path.dirname(os.path.abspath(__file__))

    if common.DEBUG: studentdir = './test/students'
    else:            studentdir = '../../../students'
    studentdir = os.path.abspath(os.path.join(filedir, studentdir))

    titandir = os.path.join(studentdir, 'titan-online')

    # .........................................................................

    # - for data copied and pasted from Titan Online into TextEdit, and saved
    #   as HTML
    student = re.compile(
        r'<tr>'
        + r'.*?<td.*?</td>'
        + r'.*?<td.*?</td>'
        + r'.*?<td.*?>(?P<cwid>\d{9})<.*?</td>'
        + r'.*?<td.*?<a href="mailto:(?P<email>[^"]+)">(?P<name>[^<]+)<.*?</td>'
        + r'.*?<td.*?</td>'
        + r'.*?<td.*?</td>'
        + r'.*?<td.*?</td>'
        + r'.*?<td.*?</td>'
        + r'.*?<td.*?</td>'
        + r'.*?</tr>*?',
        re.DOTALL,
    )

    students = {}

    # .........................................................................

    for entry in os.scandir(titandir):
        if entry.name.startswith('.') or not entry.is_file():
            continue

        path = os.path.join(titandir, entry.name)
        for m in student.finditer(open(path).read()):
            section = entry.name.split('.')[0]
            cwid = m.group('cwid')
            email = m.group('email')
            name = ' '.join(reversed( m.group('name').split(',', maxsplit=1) ))

            alias = name.split()
            if len(alias) == 1:
                alias = alias[0]
            elif alias[-1] in ( 'I', 'II', 'III', 'IV', ) and len(alias) > 2:
                alias = ' '.join([ alias[0], alias[-2] ])
            else:
                alias = ' '.join([ alias[0], alias[-1] ])

            students[cwid] = {
                'section': section,
                'email': email,
                'name': name,
                'alias': alias,
            }

    # .........................................................................

    private = common.importfile(os.path.join(studentdir, 'students.py'))

    for k in private.students:
        if k in students: students[k].update(private.students[k])
        else:             students[k] = private.students[k]

    # .........................................................................

    return students

# -----------------------------------------------------------------------------

students = _gen_students()

# -----------------------------------------------------------------------------

def lookup(string):
    '''Convert the given string, a short form of the student's name, to a
    string containing the student's CWID.

    The given string is interpreted as a sequence of whitespace separated
    fields.
    - If the first field contains a number, it is interpreted as the student's
      section number.
    - Each field besides the section number (if present) is interpreted as a
      short name (where a "short name" is some nonempty initial subset of a
      name).  The short name fields are matched in order against each student's
      names (first, middle, ..., last, ...), and then against their alias
      names.

    For example, if there was a student named "One Student" who's initials were
    unique, `lookup('o s')` should return that student's CWID.
    '''

    ret = None

    s = string.lower().split()

    section = None
    if s[0].isdecimal():
        section = s[0]
        s = s[1:]

    for cwid,info in students.items():
        if 'section' not in info or 'name' not in info:
            continue

        if section is not None and section != info['section']:
            continue

        n = info['name'].lower().split()
        a = info['alias'].lower().split()

        if len(s) <= len(n):
            for np,sp in zip(n, s):
                if not np.startswith(sp):
                    break
            else:
                if ret is None or ret == cwid:
                    ret = cwid
                else:
                    raise Error( 'Multiple matches found for \''+string+'\'' )

        if len(s) <= len(a):
            for ap,sp in zip(a, s):
                if not ap.startswith(sp):
                    break
            else:
                if ret is None or ret == cwid:
                    ret = cwid
                else:
                    raise Error( 'Multiple matches found for \''+string+'\'' )

    if ret is None:
        raise Error( 'No match found for \''+string+'\'' )

    return ret

