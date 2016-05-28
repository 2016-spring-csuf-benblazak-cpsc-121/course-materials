#include <cstdlib>

int main() {

    const int SIZE = 7;

    // SECTION BEGIN all
    // C++ style
    char * a = new char[SIZE];
    delete[] a;

    // C style
    char * b = (char *) malloc( sizeof(char) * SIZE );
    free(b);
    // SECTION END all

    return 0;
}
