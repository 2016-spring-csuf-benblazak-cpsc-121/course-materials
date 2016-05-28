#include <iostream>
#include <vector>

using std::cout;
using std::endl;

using std::vector;

// ----------------------------------------------------------------------------

int sum(int n) {
    if (n < 0)
        throw "error: n < 0";

    if (n == 0)
        return 0;

    return n + sum(n-1);
}

// ----------------------------------------------------------------------------

int main() {
    try {
        sum(-1);
    } catch (const char * e) {
        cout << e << endl;
    }

    vector<int> v = { sum(0) };
    for (int i = 1; i <= 5; i++)
        v.push_back(sum(i));

    for (int e : v)
        cout << e << " ";
    cout << endl;

    return 0;
}
