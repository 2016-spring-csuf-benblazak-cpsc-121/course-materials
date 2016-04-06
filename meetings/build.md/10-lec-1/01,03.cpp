#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

// ----------------------------------------------------------------------------

class SuperHero {
    protected:
        const string secretIdentity;

    public:
        SuperHero(const string & secretIdentity)
            : secretIdentity(secretIdentity) {}

        virtual ~SuperHero() = default;

        virtual void revealSecretIdentity() {
            cout << "no, i won't tell you >.<\n";
        }
};

class Superman : public SuperHero {
    private:
        int height;

    public:
        Superman(const string & secretIdentity)
            : SuperHero(secretIdentity) {

            height = 50;
        }

        virtual ~Superman() = default;

        virtual void revealSecretIdentity() {
            cout << "my secret identity is "
                 << secretIdentity
                 << " don't tell anyone\n";
        }

        void fly() {
            height += 100;
            cout << "i am flying " << height << " centimeters high\n";
        }
};

int main() {
    SuperHero * secret = new Superman("clark kent");
    SuperHero * secret2 = new SuperHero("bruce wanye");
    SuperHero * secret3 = new Superman("barry allan");
    SuperHero * secret4 = new SuperHero("diana prince");

    SuperHero * ss[] = {
        secret,
        secret2,
        secret3,
        secret4,
    };

    for (SuperHero * s : ss)
        s->revealSecretIdentity();
//     secret->fly();
//     (*secret).fly();

    delete secret;
    delete secret2;
    delete secret3;
    delete secret4;

    return 0;
}

