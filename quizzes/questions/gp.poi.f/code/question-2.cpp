#include <iostream>
using std::cout;
using std::endl;

// SECTION BEGIN all
void f(int i, int * p, int & r) {
    i += 2;
    (*p) += 2;
    r += 2;
}

int main() {
    int a = 3, b = 3, c = 3;
    f(a, &b, c);
    cout << a << " " << b << " " << c;
    return 0;
}
// SECTION END all

