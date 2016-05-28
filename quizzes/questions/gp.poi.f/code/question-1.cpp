#include <iostream>
using std::cout;
using std::endl;

int main() {

    // SECTION BEGIN all
    float f = 1.1;

    float * p = &f;
    *p = 2.2;

    float  & r = f;
    r = 3.3;

    cout << f << " " << *p << " " << r;
    // SECTION END all

    return 0;
}

