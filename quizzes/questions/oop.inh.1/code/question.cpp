#include <iostream>
using std::cout;
using std::endl;

class Rectangle {
    private:
        double length;
        double width;

    public:
        Rectangle(const double length, const double width)
            : length(length), width(width) {}

        double area() const { return length * width; }
};

class Square : public Rectangle {
    public:
        Square(const double edge)
            : Rectangle(edge, edge) {}
};

int main() {
    Rectangle r{2,3};
    Square s{5};

    cout << "area of rectangle: " << r.area() << endl;
    cout << "area of square: " << s.area() << endl;

    return 0;  // success
}

