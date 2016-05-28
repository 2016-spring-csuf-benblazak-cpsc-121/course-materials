#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN all
    for (int a = 1; a <= 5; a++) {
        for (int b = 5; b >= a; b--) {
            cout << b << " ";
        }
        cout << endl;
    }
    // SECTION END all

    return 0;
}
