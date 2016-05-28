/**
 * Small class example.
 */

#include <iostream>
#include <string>

using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

class Pencil {
    private:
        int lead;
    public:
        Pencil(int lead) : lead(lead) {}
        void write() {
            if (lead > 0)
                lead--;
            else
                cout << "can't write: out of lead!\n";
        }
};

// ----------------------------------------------------------------------------

int main() {
    Pencil p(2);
    for (int i = 0; i < 3; i++)
        p.write();

    return 0;
}

