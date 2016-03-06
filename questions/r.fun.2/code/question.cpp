#include <iostream>
using std::cout;
using std::endl;

// SECTION BEGIN max
float max(float, float);

float max(float a, float b) {
    if (a > b)
        return a;
    else
        return b;
}
// SECTION END max

// SECTION BEGIN times2
void times2(int &, int &);

void times2(int & a, int & b) {
    a *= 2;
    b *= 2;
}
// SECTION END times2

// SECTION BEGIN main
int main() {
    int a = 5, b = 3;
    cout << max(a, b) << endl;
    cout << a << " " << b << endl;
    times2(a, b);
    cout << a << " " << b << endl;
    return 0;
}
// SECTION END main
