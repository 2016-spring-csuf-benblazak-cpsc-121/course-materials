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

class Animal {
    public:
        static int counter;

        Animal() {
            counter++;
        }

        virtual ~Animal() {
            counter--;
        }

        static void showCounter() {
            cout << "there are " << counter << " animals\n";
        }

        virtual void breathe() = 0;
};

int Animal::counter = 0;

class Dog : public Animal {
    public:
        virtual void breathe() {
            cout << "dog: inhale, exhale\n";
        }
};

class Puppy : public Dog {
    public:
        virtual void breathe() {
            cout << "puppy: inhale, exhale\n";
        }
};

int main() {
    vector<Animal*> animals = { new Dog(), new Puppy(), };

    animals[0]->showCounter();
    Animal::showCounter();

    for (Animal * a : animals)
        a->breathe();

    for (Animal * a : animals)
        delete a;

    Animal::showCounter();

    return 0;
}

