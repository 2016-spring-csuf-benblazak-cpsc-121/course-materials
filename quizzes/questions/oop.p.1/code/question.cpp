/**
 * A short program to demonstrate the behavior of virtual functions.
 */

#include <iostream>
using std::cout;

// ----------------------------------------------------------------------------
// base class

class Phone {
    public:
        virtual void call() { cout << "phone call\n"; }
                void text() { cout << "phone text\n"; }
};

// ----------------------------------------------------------------------------
// child classes

class IPhone : public Phone {
    public:
        void call() { cout << "iphone call\n"; }
        void text() { cout << "iphone text\n"; }
};

class Android : public Phone {
    public:
        void call() { cout << "android call\n"; }
        void text() { cout << "android text\n"; }
};

// ----------------------------------------------------------------------------
// main

int main() {
    IPhone iphone;
    Android android;

    Phone * a = &iphone;
    Phone * b = &android;

    a->call();  // lookup starts in the instance type and goes up
    a->text();  // lookup starts in the pointer type and goes up

    b->call();  // lookup starts in the instance type and goes up
    b->text();  // lookup starts in the pointer type and goes up

    iphone.call();  // lookup starts in the instance type and goes up
    iphone.text();  // lookup starts in the instance type and goes up

    android.call();  // lookup starts in the instance type and goes up
    android.text();  // lookup starts in the instance type and goes up

    return 0;  // success
}
