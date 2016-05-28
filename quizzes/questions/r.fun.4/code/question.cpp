#include <iostream>
#include <vector>

using std::cout;
using std::endl;

using std::vector;

// ----------------------------------------------------------------------------
// prototypes

void print(const vector<int> & v);  // output the contents of v
void set_to_1(vector<int> & v);     // set every element of v to 1

// ----------------------------------------------------------------------------
// main

int main() {
    vector<int> a = { 1, 2, 3, 4, 5, };
    print(a);
    set_to_1(a);
    print(a);

    return 0;  // success
}

// ----------------------------------------------------------------------------
// definitions

void print(const vector<int> & v) {
    for (int e : v)
        cout << e << " ";
    cout << endl;
}

void set_to_1(vector<int> & v) {
    for (int & e : v)
        e = 1;
}

