#include <exception>
#include <iostream>

class MyException : public std::exception {
    public:
        const char * what() const noexcept {
            return "This is the error message for MyException";
        }
};

class MyClass {
    public:
        MyClass() { throw MyException(); }
};

int main() {
    try {
        MyClass c;
        std::cout << "It worked!\n";
    } catch (MyException & e) {
        std::cout << "It didn't work.  The error message was:\n";
        std::cout << e.what() << std::endl;
    }

    return 0;
}
