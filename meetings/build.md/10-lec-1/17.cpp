#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

using std::string;

// ----------------------------------------------------------------------------

class Professor {
    protected:
        int meanness;
        int chillness;

    public:
        virtual ~Professor() = default;

        virtual int getMeanness() { return meanness; }
        virtual int getChillness() { return chillness; }

        virtual void setMeanness(int meanness) { this->meanness = meanness; }
        virtual void setChillness(int c) { chillness = c; }
};

class HogwartsProfessor : public Professor {
    public:
        virtual ~HogwartsProfessor() = default;

        virtual void setChillness(int c) { chillness = c+10; }

        virtual void doMagic() { cout << "magic!!\n"; }
};

int main() {
    Professor * ben = new HogwartsProfessor;
    Professor * ben2 = new Professor;

    Professor * professors[] = { ben, ben2 };

    ben->setMeanness(1000);
    ben->setChillness(0);

    cout << "ben is " << ben->getMeanness() << " mean\n";
    cout << "ben has " << ben->getChillness() << " chill\n";

    delete ben;
    delete ben2;

    return 0;
}

