#include <iostream>
using std::cout;
using std::endl;

int main() {
    // SECTION BEGIN array
    int a[4] = { 0, 1, };
    int b[5];
    b[3] = 3;
    b[4] = 4;
    int c[] = { 4, 4, 4 };
    int d[3] = {};
    for (int i = 0; i < sizeof(d)/sizeof(int); i++)
        d[i] = i+1;
    // SECTION END array

    for (int i = 0; i < sizeof(a)/sizeof(int); i++)
        cout << a[i] << " ";
    cout << endl;

    for (int i = 0; i < sizeof(b)/sizeof(int); i++)
        cout << b[i] << " ";
    cout << endl;

    for (int i = 0; i < sizeof(c)/sizeof(int); i++)
        cout << c[i] << " ";
    cout << endl;

    for (int i = 0; i < sizeof(d)/sizeof(int); i++)
        cout << d[i] << " ";
    cout << endl;

    return 0;
}
