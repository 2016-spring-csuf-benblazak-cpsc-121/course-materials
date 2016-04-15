#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

// ----------------------------------------------------------------------------

vector<int> mergesort(const vector<int> & v) {
    // base case :)
    if (v.size() < 2)
        return v;

    // split into left and right
    vector<int> left(v.begin(), v.begin() + v.size()/2);
    vector<int> right(v.begin() + v.size()/2, v.end());

    // recursively sort both sides
    left = mergesort(left);
    right = mergesort(right);

    // merge
    vector<int> sorted;
    vector<int>::iterator l = left.begin();
    vector<int>::iterator r = right.begin();
    while (l < left.end() && r < right.end()) {
        if (*l <= *r) {
            sorted.push_back(*l);
            l++;
        } else {
            sorted.push_back(*r);
            r++;
        }
    }
    while (l < left.end()) {
        sorted.push_back(*l);
        l++;
    }
    while (r < right.end()) {
        sorted.push_back(*r);
        r++;
    }

    return sorted;
}

int main() {
    vector<int> v = { 7,2,0,6,3,1,4,8,7,43,2,6,8,85,3,2,5,78,7,3 };
    for (int e : v)
        cout << e << " ";
    cout << endl;
    for (int e : mergesort(v))
        cout << e << " ";
    cout << endl;

    return 0;
}

