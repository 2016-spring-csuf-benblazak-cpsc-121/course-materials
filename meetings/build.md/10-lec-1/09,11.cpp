#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

// ----------------------------------------------------------------------------

class Animal {
    protected:
        int charisma;

    public:
        Animal(int charisma) : charisma(charisma) {}

        virtual int getCharisma() {
            return charisma;
        }
};

class Penguin : public Animal {
    public:
        Penguin(int charisma) : Animal(charisma) {}

        virtual int getCharisma() {
            return charisma + 10;
        }

        void eatFish() {
            cout << "yum ^_^\n";
        }

        void dance() {
            cout << "left foot, waddle\n";
        }
};

class OtherPenguin : public Penguin {
    public:
        OtherPenguin(int charisma) : Penguin(charisma) {}

        virtual int getCharisma() {
            return charisma + 15;
        }
};

class Frog : public Animal {
    public:
        Frog(int charisma) : Animal(charisma) {}

        virtual int getCharisma() {
            return charisma -5;
        }
};

int main() {
    Animal * happy1 = new OtherPenguin(100);
    Animal * happy2 = new Penguin(100);
    Animal * unhappy1 = new Frog(100);
    Animal * unhappy2 = new Animal(100);

    Animal * animals[] = {
        happy1,
        happy2,
        unhappy1,
        unhappy2,
    };

    for (Animal * a : animals)
        cout << a->getCharisma() << endl;

    delete happy1;
    delete happy2;
    delete unhappy1;
    delete unhappy2;

    return 0;
}

