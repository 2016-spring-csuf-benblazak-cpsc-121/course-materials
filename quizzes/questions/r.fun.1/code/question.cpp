#include <iostream>
using std::cout;
using std::endl;

// SECTION BEGIN abs
int abs(int);

int abs(int i) {
    return (i > 0) ? i : -i;
}
// SECTION END abs

// SECTION BEGIN swap
void swap(int &, int &);

void swap(int & a, int & b) {
    int temp = a;
    a = b;
    b = temp;
}
// SECTION END swap

// SECTION BEGIN main
int main() {
    int a = 5, b = -7;
    cout << abs(a) << " "
         << abs(b) << endl;
    cout << a << " " << b << endl;
    swap(a,b);
    cout << a << " " << b << endl;
    return 0;
}
// SECTION END main
