#include <iostream>
using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

void inc(int & a);             // increment the integer
int min(int a, int b);         // return the minimum of 2 integers
int min(int a, int b, int c);  // return the minimum of 3 integers

// ----------------------------------------------------------------------------

int main() {
    // set and output initial values
    int a = 2, b = 1, c = 3;
    cout << a << " " << b << " " << c << endl;

    // test the two `min` functions, and output current values
    cout << min(a,b) << endl;
    cout << min(a,b,c) << endl;
    cout << a << " " << b << " " << c << endl;

    // test the `inc` function, and output current values
    inc(a);
    cout << a << " " << b << " " << c << endl;

    return 0;  // success
}

// ----------------------------------------------------------------------------

void inc(int & a) {
    a++;
}

int min(int a, int b) {
    return (a < b) ? a : b;
}

int min(int a, int b, int c) {
    return min( min(a, b), c );
}
