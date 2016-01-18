#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import collections
import re

# -----------------------------------------------------------------------------

class Error(Exception):
    pass

# -----------------------------------------------------------------------------

groups = collections.OrderedDict((
    (
        'assignment completion',
        (
            '',
        ),
    ),
    (
        'general knowledge',
        (
            'history and culture',
            'design',
            'review',
            'general programming',
            'object-oriented programming',
        ),
    ),
    (
        'design',
        (
            'debugging and testing correctness',
            'pseudocode',
            'documentation',
            'consistency of style',
        ),
    ),
    (
        'review',
        (

            'visual studio',
            'data types and representation',
            'operators',
            'control flow',
            'arrays',
            'functions',
            'file I/O',
        ),
    ),
    (
        'general programming',
        (
            'recursion',
            'searching, sorting, and algorithm analysis',
            'type declarations',
            'pointers and references',
            'memory management and dynamic memory',
            'templates',
            'standard library',
            'parallel arrays',
        ),
    ),
    (
        'object-oriented programming',
        (
            'classes',
            'interfaces',
            'inheritance',
            'polymorphism',
            'exceptions',
        ),
    ),
))

multipliers = {
          ('assignment completion',): 0.05,
              ('general knowledge',): 0.05,
                         ('design',): 0.15,
                         ('review',): 0.15,
            ('general programming',): 0.30,
    ('object-oriented programming',): 0.30,
}
for g,ss in groups.items():
    for s in ss:
        multipliers[(g,s)] = multipliers[(g,)]/len(groups[g])

# .............................................................................
# error check

if sum([m for g,m in multipliers.items() if len(g) == 1]) != 1:
    raise Error( 'Group multipliers do not sum to 1' )

for g,m in {g:m for g,m in multipliers.items() if len(g) == 1}.items():
    if m*100 != round(m*100):
        raise Error( 'Fractional percent in multiplier \'{}\': {}'.format(g,m) )

# -----------------------------------------------------------------------------

def long(string):
    '''Convert the given string to a tuple of the form used to index
    `multipliers`.  For example, `long('oop.c')` should return
    `('object-oriented programming', 'classes')`.
    '''

    d = groups
    ret = []

    for s in string.lower().split('.'):
        match = None

        if d is None:
            raise Error( 'No match found for \''+string+'\'' )

        for k in d:
            first_letters = ''.join([ s[:1] for s in re.split(r'\W+', k) ])
            if s == first_letters.lower() or k.lower().startswith(s):
                if match is None:
                    match = k
                else:
                    raise Error( 'Multiple matches found for \''+string+'\'' )

        if match is not None:
            ret.append(match)
            if isinstance(d, dict):
                d = d[match]
            else:
                d = None  # raise Error on next iteration, if there is one
        else:
            raise Error( 'No match found for \''+string+'\'' )

    return tuple(ret)

