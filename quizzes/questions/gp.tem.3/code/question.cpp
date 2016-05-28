#include <iostream>
#include <string>

using std::cout;
using std::endl;

using std::string;

// ----------------------------------------------------------------------------
// simple fixed-size array with bounds checking

template <typename T>
class Array11 {
    private:
        T data[11] = {};

    public:
        T get(int index) const;
        void set(int index, T value);
};

// ............................................................................
// definitions

template <typename T>
T Array11<T>::get(int index) const {
    if (index < 0 || index >= 11)
        throw "error: index out of range";
    return data[index];
}

template <typename T>
void Array11<T>::set(int index, T value) {
    if (index < 0 || index >= 11)
        throw "error: index out of range";
    data[index] = value;
}

// ----------------------------------------------------------------------------
// main

int main() {
    Array11<string> a;

    a.set(1, "hello");
    a.set(3, "world");

    cout << a.get(1) << " " << a.get(3) << endl;

    return 0;  // success
}
