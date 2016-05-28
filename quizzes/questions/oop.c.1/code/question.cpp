/**
 * Short program to make 3 characters from Avatar say their name and what
 * element(s) they bend.
 */

#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

// ----------------------------------------------------------------------------

class AvatarCharacter {
    private:
        string name;
        string element;

    public:
        AvatarCharacter(const string & name = "", const string & element = "")
            : name(name), element(element) {}

        void sayName();
        void sayElement();
};

void AvatarCharacter::sayName() {
    cout << "My name is " << name << endl;
}

void AvatarCharacter::sayElement() {
    cout << "I bend " << element << endl;
}

// ----------------------------------------------------------------------------

int main() {
    AvatarCharacter characters[] = {
        AvatarCharacter("Aang", "everything!"),
        AvatarCharacter("Katara", "water :)"),
        AvatarCharacter("Sokka", "nothing :("),
    };

    for (int i = 0; i < 3; i++) {
        characters[i].sayName();
        characters[i].sayElement();
    }
    
    return 0;  // success
}
