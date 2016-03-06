#include <iostream>

using std::cout;
using std::endl;

// SECTION BEGIN function
int factorial(int n) {
    if (n < 0)
        return 0;

    if (n == 0)
        return 1;

    return n * factorial(n-1);
}
// SECTION END function

// SECTION BEGIN main
int main() {
    for (int i = -1; i <= 5; i++)
        cout << factorial(i) << " ";

    return 0;
}
// SECTION END main
