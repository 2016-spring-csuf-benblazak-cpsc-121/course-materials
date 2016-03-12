#include <iostream>

using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

template <typename T>
class Complex {
    public:
        T r;  // real part
        T i;  // imaginary part

        Complex<T> add(const Complex<T> & c) const;
};

template <typename T>
Complex<T> Complex<T>::add(const Complex<T> & c) const {
    return Complex<T>{ r + c.r, i + c.i };
}

// ----------------------------------------------------------------------------

int main() {
    Complex<int> a, b;
    a.r = 1; a.i = 2;
    b.r = 3; b.i = 4;

    Complex<int> c = a.add(b);

    cout << c.r << " + " << c.i << "i\n";

    return 0;
}
