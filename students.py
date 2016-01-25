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

    if common.DEBUG: studentdir = './test/students'
    else:            studentdir = '../../../students'

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
            name = m.group('name')

            students[cwid] = {}
            students[cwid]['section'] = section
            students[cwid]['email'] = email
            students[cwid]['name'] = \
                    ' '.join( reversed(name.split(',', maxsplit=1)) )

    # .........................................................................

    sys.path.insert(0, studentdir)
    import students as private
    del sys.path[0]

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
    - If there are two non-numeric fields, they are interpreted as the
      student's short first name and short last name, in that order.
      Otherwise, the first non-numeric field is interpreted as the student's
      short first name, the second as the student's short first middle name (if
      present), etc., where a "short name" is some nonempty initial subset of a
      name.

    For example, if there was a student named "One Student" who's initials were
    unique, `lookup('o s')` should return that student's CWID.
    '''

    ret = None

    s = string.split()

    section = None
    if s[0].isdecimal():
        section = s[0]
        s = s[1:]

    for cwid,other in students.items():
        n = other['name'].split()

        if section is not None and section != other['section']:
            continue

        if len(s) > len(n):
            continue

        if len(s) == 2:
            n = [ n[0], n[-1] ]

        for np,sp in zip(n, s):
            if not np.lower().startswith(sp.lower()):
                break
        else:
            if ret is None:
                ret = cwid
            else:
                raise Error( 'Multiple matches found for \''+string+'\'' )

    if ret is None:
        raise Error( 'No match found for \''+string+'\'' )

    return ret

