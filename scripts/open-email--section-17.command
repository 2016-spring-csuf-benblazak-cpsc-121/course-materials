#! /bin/bash
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

cd "$(dirname "$0")"

arg=${0#*--}
arg=${arg%.*}

./open-email.py ${arg}

