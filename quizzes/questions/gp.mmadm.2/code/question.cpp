#include <cstdlib>

int main() {

    const int SIZE = 7;

    // SECTION BEGIN all
    // C++ style
    float * a = new float[SIZE];
    delete[] a;

    // C style
    float * b = (float *) malloc( sizeof(float) * SIZE );
    free(b);
    // SECTION END all

    return 0;
}
