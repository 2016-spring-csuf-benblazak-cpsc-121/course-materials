#include <iostream>
using std::cout;
using std::endl;

int main() {
    int a, b;

    a = 1; b = 1;
    cout << a << " " << b << " ";
    cout << ++a << " " << b++ << " ";
    cout << a << " " << b << endl;

    for (int i = 0; i <= 9; i++)
        cout << ( i % 3 ) << " ";
    cout << endl;

    cout << ( 'a' == 'b' || 'c' ) << endl;

    return 0;
}
