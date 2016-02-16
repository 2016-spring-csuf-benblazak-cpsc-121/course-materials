/* ----------------------------------------------------------------------------
 * Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
 * Released under the [MIT License] (http://opensource.org/licenses/MIT)
 * ------------------------------------------------------------------------- */

/**
 * Short program to create a few `Square`s and ask them to `draw` themselves.
 */

#include "rectangle.h"

// ----------------------------------------------------------------------------

int main() {
    Rectangle rectangles[] = {
        Rectangle(1,1),
        Rectangle(2,2),
        Rectangle(5,3),
        Rectangle(7,4),
        Rectangle(9,5),
    };

    for (Rectangle r : rectangles)
        r.draw();

    return 0;
}

