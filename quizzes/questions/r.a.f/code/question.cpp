#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN array
    int a[3] = { 1, };
    int b[] = { 2, 2, 2 };
    int c[3] = {};
    for (int & e : c)
        e = 3;
    int d[5];
    d[1] = 1;
    d[3] = 3;
    // SECTION END array

    for (int e : a)
        cout << e << " ";
    cout << endl;

    for (int e : b)
        cout << e << " ";
    cout << endl;

    for (int e : c)
        cout << e << " ";
    cout << endl;

    for (int e : d)
        cout << e << " ";
    cout << endl;

    return 0;
}
