#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <benblazak.dev@gmail.com>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# Project located at <https://github.com/benblazak/text-processing-utilities>
# -----------------------------------------------------------------------------

"""A script to generate student grade sheets.
"""

import os
import os.path
import shutil
import subprocess
import sys

import preppy

import common

sys.path.insert(1, '..')

import grades
import standards
import students

del sys.path[0]

# .............................................................................

filedir = os.path.dirname(os.path.abspath(__file__))

if common.DEBUG: studentdir = '../test/students'
else:            studentdir = '../../../../students'
studentdir = os.path.abspath(os.path.join(filedir, studentdir))

htmlbuilddir = os.path.join(studentdir, 'build.grades.html')
pdfbuilddir = os.path.join(studentdir, 'build.grades.pdf')

# .............................................................................

shutil.rmtree(htmlbuilddir, ignore_errors=True)
shutil.rmtree(pdfbuilddir, ignore_errors=True)

os.makedirs(htmlbuilddir)
os.makedirs(pdfbuilddir)

for cwid in students.students:
    name = students.students[cwid]['alias'].lower().replace(' ', '-')
    html = os.path.join(htmlbuilddir, name + '.html')
    pdf = os.path.join(pdfbuilddir, name + '.pdf')

    with open(html, 'w') as f:
        f.write(
            preppy.getModule(
                'gen-grade-sheet.html.preppy',
                source_extension='.preppy',
                savePyc=0
            ).get(cwid, grades, standards, students)
        )

    sp = subprocess.Popen( "wkhtmltopdf '" + html + "' '" + pdf + "'",
                           shell = True,
                           stdout = subprocess.DEVNULL,
                           stderr = subprocess.DEVNULL,
                           universal_newlines = True )

