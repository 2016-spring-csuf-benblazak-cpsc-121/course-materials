#include <iostream>
using std::cout;
using std::endl;

int main() {
    int a, b;

    a = 2; b = 2;
    cout << a << " " << b << " ";
    cout << --a << " " << b-- << " ";
    cout << a << " " << b << endl;

    for (int i = 0; i <= 9; i++)
        cout << ( i % 4 ) << " ";
    cout << endl;

    cout << ( 'x' == 'y' || 'z' ) << endl;

    return 0;
}
