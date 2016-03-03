/* ----------------------------------------------------------------------------
 * Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
 * Released under the [MIT License] (http://opensource.org/licenses/MIT)
 * ------------------------------------------------------------------------- */

/**
 * Tying it all together.
 */

#include <iostream>

#include "test.h"

using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

int main() {
    test_exceptions();  cout << "\n-------\n\n";
    test_templates();   cout << "\n-------\n\n";
    test_stl();

    return 0;
}

