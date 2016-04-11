#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

using std::ostream;

// ----------------------------------------------------------------------------

class Bread {
};

class CinnamonRoll {
    private:
        bool hasOwner;
        int icingLevel;

    public:
        CinnamonRoll(int icingLevel = 9000) : icingLevel(icingLevel) {
            hasOwner = false;
        }

        CinnamonRoll(const CinnamonRoll & cr) {
            cout << "copying\n";
            hasOwner = cr.hasOwner;
            icingLevel = cr.icingLevel;
        }

        CinnamonRoll(const Bread & b) {
            cout << "baking ^_^ yum\n";
            hasOwner = false;
            icingLevel = 0;
        }

        void purchase() {
            hasOwner = true;
        }

        void reportCalories() {
            cout << "there are " << icingLevel * 1000 << " calories\n";
        }

        friend ostream & operator<<(ostream & os, const CinnamonRoll & cr);
        friend bool operator>(const CinnamonRoll & a, const CinnamonRoll & b);
};

ostream & operator<<(ostream & os, const CinnamonRoll & cr) {
    os << ( cr.hasOwner ? "i have an owner!" : "i am alone in the world" )
       << endl;

    os << "my icing level is " << cr.icingLevel << endl;

    return os;
}

bool operator>(const CinnamonRoll & a, const CinnamonRoll & b) {
    return a.icingLevel > b.icingLevel;
}

int main() {
    CinnamonRoll cinnabon(5000);
    cinnabon.reportCalories();

    cinnabon.purchase();

    operator<<(cout, cinnabon);
    cout << cinnabon << cinnabon;

    cout << "-------\n";

    CinnamonRoll healthy(0);

    cout << operator>(cinnabon, healthy) << endl;
    cout << (cinnabon > healthy) << endl;

    cout << "-------\n";

    CinnamonRoll unhealthy1(cinnabon);
    CinnamonRoll unhealthy2 = cinnabon;
    CinnamonRoll unhealthy3;
    unhealthy3 = cinnabon;

    cout << "-------\n";

    Bread b;
    CinnamonRoll plain1(b);
    CinnamonRoll plain2 = b;

    cout << "-------\n";

    cout << (CinnamonRoll)b;
    cout << CinnamonRoll(b);
    cout << static_cast<CinnamonRoll>(b);

    return 0;
}

