#include <cstdlib>

int main() {

    const int SIZE = 7;
    // SECTION BEGIN all
    // C++ style
    double * a = new double[SIZE];
    delete[] a;
    // C style
    double * b = (double *) malloc( sizeof(double) * SIZE );
    free(b);
    // SECTION END all

    return 0;
}
