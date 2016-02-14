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
import textwrap

import common

# .............................................................................

filedir = os.path.dirname(os.path.abspath(__file__))
os.chdir(filedir)

sys.path.insert(1, '..')

import students

del sys.path[0]

# .............................................................................

if common.DEBUG: studentdir = '../test/students'
else:            studentdir = '../../../../students'
studentdir = os.path.abspath(os.path.join(filedir, studentdir))

scandir = os.path.join(studentdir, 'scans')
gradedir = os.path.join(studentdir, 'build.grades.pdf')

# -----------------------------------------------------------------------------

# all: send an email to everyone (maybe containing only an updated grade sheet)
# new: send an email to only those students with a newly graded quiz

if len(sys.argv) == 1:
    arg = 'new'
elif len(sys.argv) == 2:
    arg = sys.argv[1]
    if arg not in ( 'all', 'new' ):
        print('ERROR: unknown argument \'' + arg + '\'')
        sys.exit(1)
else:
    print('ERROR: too many arguments')
    sys.exit(1)

# .............................................................................

def gen_email(f, to, subject, body, attachments=None):
    if attachments is None: attachments = []

    boundary = 'CONTENTBOUNDARY'
    body = body.replace('=','=3D')

    email = ''

    email += textwrap.dedent( '''
        To: {to}
        From: {f}
        Subject: {subject}
        Content-Type: multipart/mixed; boundary={boundary}

        To view this message properly, please use a MIME enabled client.
    
        --{boundary}
        Content-Type: text/plain
        Content-Transfer-Encoding: quoted-printable

    '''.format(**locals()) )
    email += body

    for name,path in attachments:
        sp = subprocess.Popen( "base64 '" + path + "'",
                               shell = True,
                               stdout = subprocess.PIPE,
                               universal_newlines = True )
        base64 = '\n'.join(textwrap.wrap(sp.stdout.read()))

        ext = name.split('.')[-1]
        mime = 'text/plain'
        if ext == 'html':
            mime = 'text/html'
        elif ext == 'pdf':
            mime = 'application/pdf'

        email += textwrap.dedent( '''
            --{boundary}
            Content-Type: {mime}
            Content-Transfer-Encoding: base64
            Content-Disposition: attachment; filename={name}
        '''.format(**locals()) )
        email += '\n' + base64 + '\n'

    email += '\n--' + boundary + '--\n'

    return email

def send_email(*args):
    tempfile = os.path.abspath(os.path.join(
        filedir, 'send-grade-emails--temp.eml'
    ))

    with open(tempfile, 'w') as f:
        f.write(gen_email(*args))

    script = textwrap.dedent('''
        osascript <<END
        tell application "Mail"
            open "{tempfile}"
            activate
        end tell
        delay 1
        tell application "System Events" to ¬
            keystroke "d" using {{command down, shift down}}
        tell application "System Events" to ¬
            keystroke "d" using {{command down, shift down}}
        END
    ''').format(**locals())

    sp = subprocess.Popen( script, shell = True )
    sp.communicate()

    os.remove(tempfile)

# .............................................................................

sp = subprocess.Popen( './gen-grade-sheets--pdf.command', shell = True )
sp.communicate()

files = {}

for d in os.listdir(scandir):
    if d.startswith('.'): continue

    for f in os.listdir(os.path.join(scandir, d)):
        if f.startswith('.'): continue
        if len(f.split('.')) > 2 and f.split('.')[-2] == 'sent': continue

        cwid = students.lookup(os.path.basename(f).split(',')[0])

        fname = ( '-'.join(os.path.basename(d).split(',')[:2])
                  + '--'
                  + students.students[cwid]['alias'].lower().replace(' ','-')
                  + '.' + os.path.basename(f).split('.')[-1] )

        if cwid not in files: files[cwid] = []
        files[cwid].append([fname, os.path.join(scandir, d, f)])

for f in os.listdir(gradedir):
    if f.startswith('.'): continue
    if f.startswith('_'): continue

    cwid = students.lookup(os.path.basename(f).split('.')[0])

    fname = ( 'grade-sheet--'
              + students.students[cwid]['alias'].lower().replace(' ','-')
              + '.' + os.path.basename(f).split('.')[-1] )

    if arg in ( 'all', ) or cwid in files:
        if cwid not in files: files[cwid] = []
        files[cwid].append([fname, os.path.join(gradedir, f)])

for cwid,attachments in files.items():
    alias = students.students[cwid]['alias']

    f = 'Ben Blazak <bblazak@fullerton.edu>'
    to = alias + ' <' + students.students[cwid]['email'] + '>'

    subject = '[CPSC 121] grades'

    body = textwrap.dedent( '''\
        Dear {alias},

        Your updated grade sheet is attached, along with any graded quizzes which have not previously been sent.  Please let me know if you find any errors, or if you have any questions.  Available answer keys for quizzes will be posted to Google Drive: https://drive.google.com/folderview?id=0By3dRR4gD9xtOTZjVm5MMElqeVE&usp=sharing .

        Sincerely,
        Ben Blazak
    '''.format(**locals()) )

    send_email(f, to, subject, body, attachments)

    for attachment in attachments:
        old = attachment[1]
        new = old.rsplit('.', maxsplit=1)
        new = new[0] + '.sent.' + new[1]

        shutil.move(old, new)

