#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

template <typename T>
class Book {
    private:
        T pagelength;
        T author;
    public:
        Book(T pagelength, T author);

        void open();

        T getPagelength();
        T getAuthor();

        void setPagelength(T pagelength);
};

template <typename T>
Book<T>::Book(T pagelength, T author)
: pagelength(pagelength), author(author) {}


template <typename T>
void Book<T>::open() {
    cout << "this book is so good\n";
}


template <typename T>
T Book<T>::getPagelength() {
    return pagelength;
}

template <typename T>
T Book<T>::getAuthor() {
    return author;
}

template <typename T>
void Book<T>::setPagelength(T pagelength) {
    this->pagelength = pagelength;
}

int main() {
    Book<string> b{"2", "ben blazak"};
    b.setPagelength("a lot!");
    cout << "author " << b.getAuthor()
         << " wrote " << b.getPagelength() << " pages!\n";
    b.open();

    return 0;
}

