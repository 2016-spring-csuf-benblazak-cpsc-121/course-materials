#! /usr/bin/env python3 -B
# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

import importlib.machinery
import os.path

# -----------------------------------------------------------------------------

# DEBUG = True
DEBUG = False

# .............................................................................

org = '2016-spring-csuf-benblazak-cpsc-121'

# -----------------------------------------------------------------------------

def importfile(path, name=None):
    if name is None:
        name = os.path.basename(path).rsplit('.',maxsplit=1)[0]

    return importlib.machinery.SourceFileLoader( name, path ).load_module()

