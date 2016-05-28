#include <iostream>

using std::cout;
using std::endl;

// SECTION BEGIN function
int pow(int base, int exponent) {
    // error check
    if (exponent < 0)
        throw "error: exponent is less than 0";

    // base case
    if (exponent == 0)
        return 1;

    // recursive case
    return base * pow(base, exponent-1);
}
// SECTION END function

// SECTION BEGIN main
int main() {
    try {
        pow(2, -1);
    } catch (const char * e) {
        cout << e << endl;
    }
    for (int i = 0; i <= 5; i++)
        cout << pow(2, i) << " ";
    cout << endl;

    return 0;
}
// SECTION END main
