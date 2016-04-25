#include <iostream>

using std::cout;
using std::endl;

// SECTION BEGIN function
int sumEven(int n) {
    if (n < 0)
        throw "error: n is less than 0";

    if (n == 0)
        return 0;

    if (n%2)
        return sumEven(n-1);

    return n + sumEven(n-2);
}
// SECTION END function

// SECTION BEGIN main
int main() {
    try {
        sumEven(-1);
    } catch (const char * e) {
        cout << e << endl;
    }
    for (int i = 0; i <= 5; i++)
        cout << sumEven(i) << " ";
    cout << endl;

    return 0;
}
// SECTION END main
