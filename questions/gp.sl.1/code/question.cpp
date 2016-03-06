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
    vector<int> v = { 1, 2, 3, };
    v.push_back(4);
    v[1] = 5;
    print_vector(v);

    return 0;
}
