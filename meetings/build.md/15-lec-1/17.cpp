#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

// ----------------------------------------------------------------------------

void f(int n) {
    cout << "start f\n";
    if (n < 1) throw "error";
    cout << "end f\n";
}

void g(int n) {
    cout << "start g\n";
    try {
        f(n);
    } catch (const char * e) {
        cout << e << endl;
        throw;
    }
    cout << "end g\n";
}

int main() {
    cout << "start main\n";

    try {
        cout << "start try 1\n";
        g(1);
        cout << "end try 1\n";
    } catch (const char e[]) {
        cout << e << endl;
    }
    try {
        cout << "start try 2\n";
        g(-1);
        cout << "end try 2\n";
    } catch (const char e[]) {
        cout << e << endl;
    }

    cout << "end main\n";

    return 0;
}

