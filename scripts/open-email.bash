#! /bin/bash
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

cd "$(dirname "$0")"

osascript <<END
$(cat open-email.applescript)
openEmail($(./open-email.py $([ $# -ge 1 ] && echo "$1")))
tell application "Mail" to activate
END

