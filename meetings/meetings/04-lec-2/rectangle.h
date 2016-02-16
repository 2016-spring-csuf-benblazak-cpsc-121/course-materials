/* ----------------------------------------------------------------------------
 * Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
 * Released under the [MIT License] (http://opensource.org/licenses/MIT)
 * ------------------------------------------------------------------------- */

/**
 * A class representing a simple model of a Rectangle.
 */

#ifndef RECTANGLE_H
#define RECTANGLE_H
// ----------------------------------------------------------------------------

class Rectangle {
    private:
        int width;
        int height;

    public:
        Rectangle(int w, int h);
        void draw() const;
};

// ----------------------------------------------------------------------------
#endif

