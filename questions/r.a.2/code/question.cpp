#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN array
    int a[4] = { 3, 2, };
    int b[] = { 4, 4, 4 };
    int c[3] = {};
    for (int i = 0; i < 3; i++)
        c[i] = i*i;
    int d[5];
    d[3] = 3;
    d[4] = 4;
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
