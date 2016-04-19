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

void ss(vector<int> & v) {
    for (int a = 0; a < v.size(); a++) {
        int min = a;
        for(int b = a+1; b < v.size(); b++) {
            if (v[b] < v[min])
                min = b;
        }
        int temp = v[a];
        v[a] = v[min];
        v[min] = temp;
    }
}

int main() {
    vector<int> v = { 7,3,1,2,6,8,8,5,32,23,56,8,0,6,4,2, };
    for (int e : v)
        cout << e << " ";
    cout << endl;
    ss(v);
    for (int e : v)
        cout << e << " ";
    cout << endl;

    return 0;
}

