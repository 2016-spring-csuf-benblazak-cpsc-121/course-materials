#include <iostream>
using std::cin;
using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

int main() {
    // ------------------------------------------------------------------------

    {
        cout << "// SECTION BEGIN scope--bad\n";
        for (int i = 0; i < 5; i++)
            for (i = 0; i < 5; i++)
                cout << i << " ";
        cout << endl;
        cout << "// SECTION END scope--bad\n";
    }
    {
        cout << "// SECTION BEGIN scope--good\n";
        for (int i = 0; i < 5; i++)
            for (int i = 0; i < 5; i++)
                cout << i << " ";
        cout << endl;
        cout << "// SECTION END scope--good\n";
    }

    // ------------------------------------------------------------------------

    return 0;
}

