#include <iostream>
using std::cout;
using std::endl;

int main() {

    // SECTION BEGIN all
    char c = 'a';

    char * p = &c;
    *p = 'b';

    char & r = c;
    r = 'c';

    cout << c << " " << *p << " " << r;
    // SECTION END all

    return 0;
}

