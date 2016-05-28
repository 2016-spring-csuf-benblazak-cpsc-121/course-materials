#include <iostream>

using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

template <typename T>
class Point {
    public:
        T x;
        T y;

        Point<T> add(const Point<T> & p) const;
};

template <typename T>
Point<T> Point<T>::add(const Point<T> & p) const {
    return Point<T>{ x + p.x, y + p.y };
}

// ----------------------------------------------------------------------------

int main() {
    Point<float> a, b;
    a.x = 1.1; a.y = 2.2;
    b.x = 3.3; b.y = 4.4;

    Point<float> c = a.add(b);

    cout << "(" << c.x << ", " << c.y << ")\n";

    return 0;
}
