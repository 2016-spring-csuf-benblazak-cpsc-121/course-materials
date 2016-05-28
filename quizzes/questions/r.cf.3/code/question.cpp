#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN all
    for (int a = 5; a >= 1; a--) {
        cout << "+ ";
        for (int b = 5; b >= a; b--) {
            cout << a << " ";
        }
        cout << "- " << endl;
    }
    // SECTION END all

    return 0;
}
