#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN all
    for (int a = 1; a <= 5; a++) {
        for (int b = 1; b <= a; b++) {
            cout << a << " ";
        }
        cout << endl;
    }
    // SECTION END all

    return 0;
}
