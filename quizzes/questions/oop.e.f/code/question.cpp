/**
 * A short example of exceptions.
 */

#include <iostream>
using std::cout;
using std::endl;

void f() {
    cout << "f start\n";
    throw "exception!";
    cout << "f end\n";
}

void g() {
    cout << "g start\n";
    f();
    cout << "g end\n";
}

int main() {
    cout << "main start\n";
    try {
        g();
    } catch (const char * e) {
        cout << e << endl;
    }
    cout << "main end\n";

    return 0;
}
