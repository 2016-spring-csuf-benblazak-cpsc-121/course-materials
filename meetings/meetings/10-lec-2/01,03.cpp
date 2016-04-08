#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

using std::ostream;

// ----------------------------------------------------------------------------

class Car {
};

class Food {
    private:
        bool isDelicious;
        bool isEdible;

    public:
        Food() {
            isDelicious = false;
            isEdible = false;
        }

        Food(const Food & f) {
            cout << "copying\n";
            isDelicious = f.isDelicious;
            isEdible = f.isEdible;
        }

        Food(const Car & c) {
            cout << "converting\n";
            isDelicious = false;
            isEdible = false;
        }

        void beCooked(bool cookedNicely) {
            cout << "ouch -_-\n";
            if (cookedNicely) {
                isDelicious = true;
                isEdible = true;
                cout << "i am now delicious and edible :)\n";
            }
        }

        friend Food operator+(const Food & a, const Food & b);
        friend ostream & operator<<(ostream & os, const Food & f);
};

Food operator+(const Food & a, const Food & b) {
    Food c;
    c.isDelicious = true;
    c.isEdible = true;
    cout << "adding food\n";
    return c;
}

ostream & operator<<(ostream & os, const Food & f) {
    cout << "this food is" << ( f.isDelicious ? "" : " not" ) << " delicious\n";
    cout << "this food is" << ( f.isEdible ? "" : " not" ) << " edible\n";

    return os;
}

int main() {
    Food apple;
    Food pie;

    pie.beCooked(true);

    Food sugar = apple + pie;

    operator<<(cout, apple);
    cout << apple;

    cout << "-------\n";

    Food carrots = pie;
    carrots = pie;

    cout << carrots;

    cout << "-------\n";

    Car mustang;
    Food celery = mustang;

    cout << Food(mustang);
    cout << (Food)mustang;
    cout << static_cast<Food>(mustang);

    return 0;
}

