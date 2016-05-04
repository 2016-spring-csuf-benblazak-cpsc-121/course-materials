#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

// ----------------------------------------------------------------------------

class Doctor {
    private:
        int assistants;
        int patients;
    public:
        virtual void operate() { cout << "operate\n"; }
        void diagnose() { cout << "diagnose\n"; };
};

class RealDoctor : public Doctor {
    public:
        void operate() { cout << "real operate\n"; }
        void diagnose() { cout << "real diagnose\n"; }
};

class FakeDoctor : public Doctor {
    public:
        void operate() { cout << "fake operate\n"; }
        void diagnose() { cout << "fake diagnose\n"; }
};

int main() {
    RealDoctor realdoctor;
    FakeDoctor fakedoctor;

    Doctor * rd = &realdoctor;
    Doctor * fd = &fakedoctor;

    rd->operate();  // real operate
    rd->diagnose(); // diagnose

    fd->operate();  // fake operate
    fd->diagnose(); // diagnose

    realdoctor.operate();  // real operate
    realdoctor.diagnose(); // real diagnose

    fakedoctor.operate();  // fake operate
    fakedoctor.diagnose(); // fake diagnose

    return 0;
}

