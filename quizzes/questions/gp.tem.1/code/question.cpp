#include <iostream>
using std::cout;
using std::endl;
// ----------------------------------------------------------------------------
// a class template to hold 10 elements of any type, in a simple stack
template <typename T>
class Stack10 {
    private:
        static const int SIZEMAX = 10;  // the maximum number of elements
        int size = 0;                   // the current number of elements
        T data[SIZEMAX] = {};           // an array containing the elements
    public:
        void push(T e);  // push an element onto the top of the stack
        T pop();         // remove an element from the top of the stack
};
template <typename T>
void Stack10<T>::push(T e) {
    if (size == SIZEMAX) throw "error: stack is full";
    data[size] = e;
    size++;
}
template <typename T>
T Stack10<T>::pop() {
    if (size == 0) throw "error: stack is empty";
    T temp = data[size-1];
    size--;
    return temp;
}
// ----------------------------------------------------------------------------
int main() {
    Stack10<int> s;
    for (int i = 0; i < 5; i++)
        s.push(i*i);
    // instead of checking when the stack is empty, just remove elements until
    // an exception is thrown.  some people would consider this an abuse of
    // exceptions, but some people like the paradigm.  this type of thing
    // (usually behind the scenes) is common in python.
    try {
        for(;;)
            cout << s.pop() << " ";
    } catch (const char * e) {
        cout << endl;
    }
    return 0;
}
