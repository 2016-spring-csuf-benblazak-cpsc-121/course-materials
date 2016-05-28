#include <iostream>
using std::cout;
using std::endl;

int main() {
    int a, b;

    a = 7; b = 7;
    cout << a << " " << b << " ";
    cout << ++a << " " << b++ << " ";
    cout << a << " " << b << endl;

    for (int i = 0; i <= 9; i++)
        cout << ( i % 5 ) << " ";
    cout << endl;

    cout << ( 1 == 2 || 3 ) << endl;

    return 0;
}
