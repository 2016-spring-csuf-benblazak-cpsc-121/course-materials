// SECTION BEGIN all
/**
 * A base class for the characters of an imaginary RPG.
 */
class Person {
    private:
        int body;
        int soul;
        int mind;
        int magic;

    public:
        virtual ~Person() = default;

        virtual int getBody() { return body; }
        virtual int getSoul() { return soul; }
        virtual int getMind() { return mind; }
        virtual int getMagic() { return magic; }

        virtual void setBody(int body) { this->body = body; }
        virtual void setSoul(int soul) { this->soul = soul; }
        virtual void setMind(int mind) { this->mind = mind; }
        virtual void setMagic(int magic) { this->magic = magic; }

        virtual void attack() = 0;
        virtual void defend() = 0;
        virtual void heal() = 0;
        virtual void cast() = 0;
};
// SECTION END all

int main() {
    return 0;
}

