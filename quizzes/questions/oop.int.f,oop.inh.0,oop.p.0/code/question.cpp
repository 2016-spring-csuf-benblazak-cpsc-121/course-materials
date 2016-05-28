/**
 * A short example of interfaces, inheritance, and polymorphism.
 */

#include <iostream>
using std::cout;

// ----------------------------------------------------------------------------

class Monster {
    public:
        virtual ~Monster() = default;
        virtual void smash() = 0;
};

class Godzilla : public Monster {
    public:
        void smash() { cout << "smash!!!\n"; }
        void jump() { cout << "jump!!!\n"; }
};

class NiceGodzilla : public Godzilla {
    public:
        void smash() { cout << "nice smash!!!\n"; }
        void jump() { cout << "nice jump!!!\n"; }
};

// ----------------------------------------------------------------------------

int main() {
    Godzilla g;
    NiceGodzilla ng;
    Monster * mp;
    Godzilla * gp;

    mp = &g;  mp->smash();
    mp = &ng; mp->smash();

    gp = &g;  gp->smash(); gp->jump();
    gp = &ng; gp->smash(); gp->jump();

    return 0;
}

