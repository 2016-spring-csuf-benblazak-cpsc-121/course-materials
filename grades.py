#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

# TODO

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

