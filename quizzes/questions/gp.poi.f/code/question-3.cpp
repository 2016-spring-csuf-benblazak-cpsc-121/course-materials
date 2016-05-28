#include <cstdint>

#include <iostream>
using std::cout;
using std::endl;

int main() {
    int a[] = { 7, 8, 9, 10, 11, };
    int * p = a;

    cout << ( (uintptr_t)a == (uintptr_t)&a ) << " "  // a, &a, same value?
         << ( (uintptr_t)p == (uintptr_t)&p ) << " "  // p, &p, same value?
         << endl;

    cout << a[0] << " " << p[0] << " " << *a     << " " << *p     << " "
         << a[2] << " " << p[2] << " " << *(a+2) << " " << *(p+2) << " "
         << endl;

    cout << sizeof(a) << " "  // assuming `sizeof(int)` is 4
         << sizeof(p) << " "  // on a typical 64 bit system
         << endl;

    return 0;
}
