#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

using std::ostream;

// ----------------------------------------------------------------------------

class Other {
    public:
        int a;
        int b;
};

class Car {
    private:
        int gas;
        int electricity;

    public:
        Car(int gas, int electricity) : gas(gas), electricity(electricity) {
            cout << "starting car\n";
        }

        ~Car() {
            cout << "stopping car\n";
        }

        Car(Other & o) {
            gas = o.a;
            electricity = o.b;
        }

        void drive() const {
            cout << "vroom vroom\n";
        }

        friend ostream& operator<<(ostream & os, const Car & c);
        friend Car operator+(const Car & a, const Car & b);
};

ostream& operator<<(ostream & os, const Car & c) {
    cout << "gas: " << c.gas << " electricity: " << c.electricity << endl;
    c.drive();

    return os;
}

Car operator+(const Car & a, const Car & b) {
    return Car{ a.gas + b.gas, a.electricity + b.electricity };
}

int main() {
    Car * audi = new Car(30, 0);
    Car * prius = new Car(10, 50);

    cout << *audi;
    cout << *prius;
    cout << ( *audi + *prius );

    cout << "-------\n";

    Other o;
    o.a = 5;
    o.b = 10;

    Car car = o;
    cout << car;

    delete audi;
    delete prius;

    return 0;
}

