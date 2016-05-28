#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN all
    for (int a = 5; a >= 1; a--) {
        cout << "hello :) ";
        for (int b = a; b >= 1; b--) {
            cout << b << " ";
        }
        cout << endl;
    }
    // SECTION END all

    return 0;
}
