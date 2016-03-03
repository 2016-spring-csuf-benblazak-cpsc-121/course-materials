/* ----------------------------------------------------------------------------
 * Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
 * Released under the [MIT License] (http://opensource.org/licenses/MIT)
 * ------------------------------------------------------------------------- */

/**
 * Implements `test.h`.
 */

#include <exception>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <typeinfo>
#include <vector>

#include "test.h"

using std::cout;
using std::cin;
using std::endl;

using std::string;

using std::map;
using std::set;
using std::vector;

// ----------------------------------------------------------------------------
// exceptions
// ----------------------------------------------------------------------------

namespace {
    // since these things should be local to this file

    class Error : public std::exception {
        private:
            string message;
        public:
            Error(string message) : message("ERROR: " + message) {}

            const char * what() const noexcept {
                return message.c_str();
            }
    };

    void f() {
        cout << "start f\n";
        throw Error("this is very serious -_-");
        cout << "end f\n";
    }

    void g() {
        cout << "start g\n";
        f();
        cout << "end g\n";
    }

}

void test_exceptions() {
    cout << "start test_exceptions\n";

    try {
        g();

    } catch (const string & s) {
        cout << "caught string!\n";
        cout << "it says " << s << "\n";

    } catch (const char * s) {
        cout << "caught const char *!\n";
        cout << "it says " << s << "\n";

    } catch (const Error & e) {
        cout << "caught Error!\n";
        cout << "it says " << e.what() << endl;

    } catch (...) {
        cout << "caught -- dunno what type!\n";
    }

    cout << "end test_exceptions\n";
}

// ----------------------------------------------------------------------------
// templates
// ----------------------------------------------------------------------------

namespace {
    // since this function should be local to this file

    template <typename T>
    T add(T a, T b) {
        return a + b;
    }

    template <typename T>
    class Turtle {
        private:
            T data;
        public:
            void setData(T newData) {
                data = newData;
            }
            T getData() const {
                return data;
            }
            void speak() const {
                cout << "I am a turtle!  I am holding "
                     << data
                     << " which is of type "
                     << typeid(data).name()
                     << endl;
            }
    };
}

void test_templates() {
    cout << add(1, 2) << endl;
    cout << add(1.3, 2.3) << endl;
//     cout << add(1, 2.3) << endl;  // error

    string s1 = "hello ";
    string s2 = "world ";
    cout << add(s1, s2) << endl;

    cout << "\n.......\n\n";
    // ........................................................................

    Turtle<int> t1;     t1.setData(5);
    Turtle<string> t2;  t2.setData("hello :)");
    Turtle<double> t3;  t3.setData(3.14);

    t1.speak();
    t2.speak();
    t3.speak();
}

// ----------------------------------------------------------------------------
// stl
// ----------------------------------------------------------------------------

void test_stl() {
    // ........................................................................
    // vector
    {
        vector<int> v = {1, 2, 3, 4};

        v.push_back(7);

        for (int e : v)
            cout << e << " ";
        cout << endl;
    }
    {
        vector<string> v = { "hi", "there" };
        v.push_back("world");

        for (string e : v)
            cout << e << " ";
        cout << endl;
    }
    cout << "\n.......\n\n";
    // ........................................................................
    // set
    {
        set<int> s = {1, 2, 3, 4, 1, 2, 3, 4};
        s.insert(1);
        s.insert(2);
        s.insert(3);
        s.insert(4);
        s.insert(7);
        s.insert(7);
        s.insert(8);
        s.insert(8);

        for (int e : s)
            cout << e << " ";
        cout << endl;
    }
    {
        set<string> s = { "hi", "hi", "world!" };

        for (string e : s)
            cout << e << " ";
        cout << endl;

        s.erase("hi");

        for (string e : s)
            cout << e << " ";
        cout << endl;
    }
    cout << "\n.......\n\n";
    // ........................................................................
    // map
    {
        map<string,double> m = {{"pi", 3.14}, {"e", 2.718}};
        m["phi"] = 1.61803;

        for ( std::pair<string,double> e : m )
            cout << e.first << " equals " << e.second << endl;
    }
}

