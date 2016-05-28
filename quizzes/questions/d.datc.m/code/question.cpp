#include <iostream>
using std::cin;
using std::cout;
using std::endl;

// ----------------------------------------------------------------------------

#if 0
// SECTION BEGIN max--bad
int max(int a, int b) {
    if (a > b)
        return a;
    else if (b > a)
        return b;
}
// SECTION END max--bad
#endif
// SECTION BEGIN max--good

int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}
// SECTION END max--good

// ----------------------------------------------------------------------------

#if 0
// SECTION BEGIN void--bad
void v() {
    cout << "void!\n";
    return void;
}
// SECTION END void--bad
#endif

// SECTION BEGIN void--good
void v() {
    cout << "void!\n";
    return;  // or, in this case, `return;` may be omitted altogether
}
// SECTION END void--good

// ----------------------------------------------------------------------------
// ----------------------------------------------------------------------------

int main() {
    // ------------------------------------------------------------------------

#if 0
goto end__equals__bad;
    {
        cout << "// SECTION BEGIN equals--bad\n";
        char a;
        do {
            cout << "hello!\n";
            cout << "should i say hello again? (y/n): ";
            cin >> a;
        } while (a = 'y');
        cout << "// SECTION END equals--bad\n";
    }
end__equals__bad:
#endif
goto end__equals__good;
    {
        cout << "// SECTION BEGIN equals--good\n";
        char a;
        do {
            cout << "hello!\n";
            cout << "should i say hello again? (y/n): ";
            cin >> a;
        } while (a == 'y');
        cout << "// SECTION END equals--good\n";
    }
end__equals__good:

    // ------------------------------------------------------------------------


    {
        cout << "// SECTION BEGIN or--bad\n";
        for (int i = 1; i <= 15; i++) {
            if ( 0 == (i % 3) || (i % 5) )
                cout << "(" << i << ") ";
            else
                cout << i << " ";
        }
        cout << endl;
        cout << "// SECTION END or--bad\n";
    }
    {
        cout << "// SECTION BEGIN or--good\n";
        for (int i = 1; i <= 15; i++) {
            if ( 0 == (i % 3) || 0 == (i % 5) )
                cout << "(" << i << ") ";
            else
                cout << i << " ";
        }
        cout << endl;
        cout << "// SECTION END or--good\n";
    }

    // ------------------------------------------------------------------------

#if 0
    {
        cout << "// SECTION BEGIN infinite--bad\n";
        for (;;)
            cout << "this loop should execute precisely once\n";
            break;
        cout << "// SECTION END infinite--bad\n";
    }
#endif
    {
        cout << "// SECTION BEGIN infinite--good\n";
        for (;;) {
            cout << "this loop should execute precisely once\n";
            break;
        }
        cout << "// SECTION END infinite--good\n";
    }

    // ------------------------------------------------------------------------

goto end__for__bad;
    {
        cout << "// SECTION BEGIN for--bad\n";
        for (int i = 1; i >= 5; i++)
            cout << i << " ";
        cout << endl;
        cout << "// SECTION END for--bad\n";
    }
end__for__bad:
    {
        cout << "// SECTION BEGIN for--good\n";
        for (int i = 1; i <= 5; i++)
            cout << i << " ";
        cout << endl;
        cout << "// SECTION END for--good\n";
    }

    // ------------------------------------------------------------------------

goto end__uninitialized__bad;
    {
        cout << "// SECTION BEGIN uninitialized--bad\n";
        int a[5] = { 5, 4, 7, 6, 2, };
        int max;
        for (int i = 0; i < 5; i++)
            if (max < a[i])
                max = a[i];
        cout << max << endl;
        cout << "// SECTION END uninitialized--bad\n";
    }
end__uninitialized__bad:
    {
        cout << "// SECTION BEGIN uninitialized--good\n";
        int a[5] = { 5, 4, 7, 6, 2, };
        int max = a[0];
        for (int i = 1; i < 5; i++)
            if (max < a[i])
                max = a[i];
        cout << max << endl;
        cout << "// SECTION END uninitialized--good\n";
    }

    // ------------------------------------------------------------------------

    return 0;
}

