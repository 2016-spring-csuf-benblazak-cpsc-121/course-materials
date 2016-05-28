#include <exception>
#include <iostream>

using std::cout;
using std::endl;

// SECTION BEGIN error-class
class ErrorDivisionByZero : public std::exception {
    public:
        const char * what() const noexcept {
            return "cannot divide by zero";
        }
};
// SECTION END error-class

double divide(double a, double b) {
    if (b == 0)
        throw ErrorDivisionByZero();

    return a / b;
}

int main() {
    try {
        cout << divide(5, 3) << endl;
    } catch (const ErrorDivisionByZero & e) {
        cout << "It didn't work: " << e.what() << endl;
    }

    try {
        cout << divide(3, 0) << endl;
    } catch (const ErrorDivisionByZero & e) {
        cout << "It didn't work: " << e.what() << endl;
    }

    return 0;
}
