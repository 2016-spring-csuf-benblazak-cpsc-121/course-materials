#include <cstdlib>

int main() {

    // SECTION BEGIN all
    // C++ style
    bool * a = new bool[11];
    delete[] a;

    // C style
    bool * b = (bool *) malloc( sizeof(bool) * 11 );
    free(b);
    // SECTION END all

    return 0;
}
