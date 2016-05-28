#include <iostream>

using std::cout;
using std::endl;

// ----------------------------------------------------------------------------
// prototypes

int max(int a, int b, int c);        // return the maximum of 3 integers
void set_to_zero(int & a, int & b);  // set both integers to zero

// ----------------------------------------------------------------------------
// main

int main() {
    int a = 5, b = 3, c = 4;
    cout << a << " " << b << " " << c << endl;

    cout << max(a, b, c) << endl;
    cout << a << " " << b << " " << c << endl;

    set_to_zero(a, b);
    cout << a << " " << b << " " << c << endl;

    return 0;  // success
}

// ----------------------------------------------------------------------------
// definitions

int max(int a, int b, int c) {
    return (a >= b) ? ( (a >= c) ? a : c ) : ( (b >= c) ? b : c );
}

void set_to_zero(int & a, int & b) {
    a = 0;
    b = 0;
}

