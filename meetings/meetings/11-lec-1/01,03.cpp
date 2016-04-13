#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::ostream;
using std::string;
using std::vector;

// ----------------------------------------------------------------------------

class Vehicle {
    private:
        static int counter;

    public:
        Vehicle() {
            counter++;
        }

        virtual ~Vehicle() {
            counter--;
        }

        virtual void goForward() = 0;

        static void printCount() {
            cout << "there are " << counter << " vehicles\n";
        }
};

int Vehicle::counter = 0;

class Car : public Vehicle {
    public:
        virtual void goForward() {
            cout << "i am a car, going forward\n";
        }
};

class Rickshaw : public Vehicle {
    public:
        virtual void goForward() {
            cout << "i am human, going forward, and carrying you, 'cause you're lazy\n";
        }
};

int main() {
    vector<Vehicle*> vehicles = { new Car(), new Rickshaw(), };

    for (Vehicle * v : vehicles) {
        v->goForward();
        v->printCount();
    }

    for (Vehicle * v : vehicles)
        delete v;

    cout << "-------\n";

    Vehicle::printCount();
    Car * c = new Car();
    Vehicle::printCount();
    delete c;
    Vehicle::printCount();

    return 0;
}

