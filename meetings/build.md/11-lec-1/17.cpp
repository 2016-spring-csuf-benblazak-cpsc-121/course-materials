#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

using std::ostream;

// ----------------------------------------------------------------------------

class Organism {
    public:
        static int counter;

        static void printCounter() {
            cout << "there are " << counter << " organisms" << endl;
        }

        Organism() {
            counter++;
            cout << "constructing organism " << counter << endl;
        }

        virtual ~Organism() {
            cout << "destructing organism " << counter << endl;
            counter--;
        }

        virtual void eat() = 0;
        virtual void sleep() = 0;
};

int Organism::counter = 0;

class Cat : public Organism {
    public:

        virtual void eat() {
            cout << "i'm a cat.  yum\n";
        }
        virtual void sleep() {
            cout << "i'm a cat.  go away\n";
        }
};

class Dog : public Organism {
    public:
        virtual void eat() {
            cout << "i'm a dog.  yum!\n";
        }
        virtual void sleep() {
            cout << "i'm a dog.  play with me ^_^\n";
        }
};

int main() {
    Organism * c = new Cat;

    c->eat();
    c->sleep();

    Organism * d = new Dog;

    d->eat();
    d->sleep();

    delete c;
    delete d;

    Organism::printCounter();

    return 0;
}

