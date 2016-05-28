#include <iostream>
#include <string>

struct Person {
    std::string name;
    int age;

    Person(std::string n, int a) : name(n), age(a) {}
};

// SECTION BEGIN arrays
int main() {
    std::cout << "// SECTION BEGIN arrays\n";  // SECTION IGNORE
    std::cout << "// SECTION PAUSE arrays\n";
    // SECTION IGNORE ---------------------------------------------------------
    Person persons[] = {
        Person( "jinora", 10 ), Person( "ikki", 7 ),
        Person( "meelo", 5 ),   Person( "rohan", 0 ),
    };

    for (int i = 0; i < 4; i++)
        std::cout << persons[i].name << " is "
                  << persons[i].age << " years old\n";
    // SECTION IGNORE ---------------------------------------------------------
    std::cout << "// SECTION PAUSE all\n";

    std::cout << "// SECTION RESUME arrays\n";
    // SECTION IGNORE ---------------------------------------------------------
    std::string names[] = { "jinora", "ikki", "meelo", "rohan" };
    int          ages[] = {       10,      7,       5,       0 };

    for (int i = 0; i < 4; i++)
        std::cout << names[i] << " is "
                  << ages[i] << " years old\n";
    // SECTION IGNORE ---------------------------------------------------------
    std::cout << "// SECTION RESUME all\n";

    return 0;
}
