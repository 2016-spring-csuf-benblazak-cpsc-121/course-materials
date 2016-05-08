#include <iostream>
#include <vector>

using std::cout;
using std::endl;

using std::vector;

// ----------------------------------------------------------------------------

template <typename T>
void print_vector(const vector<T> & v) {
    for (T e : v)
        cout << e << " ";
}

// ----------------------------------------------------------------------------

int main() {
    vector<float> v = { 3.3, 2.2, 1.1, };
    v.push_back(4.4);
    v[0] = 5.5;
    print_vector(v);

    return 0;
}

