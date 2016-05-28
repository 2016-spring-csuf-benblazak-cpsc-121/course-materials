#include <iostream>
#include <vector>

using std::cout;
using std::endl;

using std::vector;

// ----------------------------------------------------------------------------

int factorial(int n) {
    if (n < 0)
        throw "error: n < 0";

    if (n == 0)
        return 1;

    return n * factorial(n-1);
}

// ----------------------------------------------------------------------------

int main() {
    try {
        factorial(-1);
    } catch (const char * e) {
        cout << e << endl;
    }

    vector<int> v;
    for (int i = 0; i <= 5; i++)
        v.push_back(factorial(i));

    for (int e : v)
        cout << e << " ";
    cout << endl;

    return 0;
}
