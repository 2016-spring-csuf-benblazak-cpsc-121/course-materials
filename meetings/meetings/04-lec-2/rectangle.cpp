/* ----------------------------------------------------------------------------
 * Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
 * Released under the [MIT License] (http://opensource.org/licenses/MIT)
 * ------------------------------------------------------------------------- */

/**
 * Implements `square.h`
 */

#include <iostream>

#include "rectangle.h"

// ----------------------------------------------------------------------------

Rectangle::Rectangle(int w, int h) : width(w), height(h) {}

void Rectangle::draw() const {
    for (int y=1; y <= height; y++) {
        for (int x=1; x <= width; x++) {
            if (y == 1 && (x == 1 || x == width))
                std::cout << ".";
            else if (y == height && (x == 1 || x == width))
                std::cout << "'";
            else if (y == 1 || y == height)
                std::cout << "-";
            else if (x == 1 || x == width)
                std::cout << "|";
            else
                std::cout << " ";
        }
        std::cout << std::endl;
    }
}

