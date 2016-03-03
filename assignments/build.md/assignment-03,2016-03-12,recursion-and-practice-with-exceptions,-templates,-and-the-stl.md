# Assignment 03: Recursion and Practice with Exceptions, Templates, and the STL
please turn in by 11pm on 2016-03-12

## Requirements

This project is to be done in groups.

You are allowed to write everything in one file this time, so long it is
organized and the file is not too long.  If the file gets too long, please
split it into multiple `.h` and `.cpp` files, and have a `main.cpp` that
`#include`s the `.h` files, and can be used to call the test functions
prototyped in them.  I recommend having one pair of `.h` and `.cpp` files for
Parts 1--3, and another pair for Part 4 (and the challenge, if you choose to
take it).

All the files you produce must be able to exist within a single project.  You
will submit these files via github as normal.


### Part 1

0. Read about exceptions (either
   [here](http://www.cplusplus.com/doc/tutorial/exceptions/),
   or you may find another source).
0. Come up with the most interesting (readable) example of using them that you
   can.  This should take an hour or less.

### Part 2

0. Read about templates (I suggest starting
   [here](https://isocpp.org/wiki/faq/templates)
   and reading till you feel like you've read enough).
0. Come up with the most interesting (readable) example of using them that you
   can.  This should take an hour or less.

### Part 3

0. Think about a time when you really wanted a variable length array, or a list
   that was always sorted, or something similar.
0. Read about `vector`s, `set`s, and one other STL container that looks
   interesting to you.  [This](http://en.cppreference.com/w/cpp/container)
   might be a good place to start, but you may also need to google around a
   bit.
0. Come up with the most interesting (readable) example of using them that you
   can.  This should take an hour or less.

### Part 4

Write definitions for as many of the following functions as you can in roughly
3 hours.  Be sure to label the base case and recursive case in each function.

- `int gcd(int a, int b);`

  Returns the greatest common divisor of two integers using Euclid's algorithm.
  This function has the following properties:

    - `gcd(a,0)` evaluates to `abs(a)`
    - `gcd(a,b)` is equivalent to `gcd(b,a)`
    - `gcd(a,b)` is equivalent to `gcd(abs(a),abs(b))`
    - `gcd(a,b)` is equivalent to `gcd(a-b,b)` is equivalent to `gcd(a,b-a)`

  Pseudocode for this function might look like the following:

    - Normalize `a` and `b` by making them positive
    - If `a` or `b` is `0`, return the one that is nonzero
    - If `a > b` return `gcd(a-b, b)`
    - Otherwise return `gcd(a, b-a)`

  where line (2) is the base case, and lines (3) and (4) are the recursive
  case.

- `int fib(int n);`

  Returns the `n`th Fibonacci number.  Recall that the Fibonacci sequence is
  defined as follows:

    - `fib(1)` evaluates to `1`
    - `fib(2)` evaluates to `1`
    - `fib(n)` evaluates to `fib(n-1) + fib(n-2)`

- `int pow(int a, int b);`

  Returns `a` raised to the `b`th power (for positive `b`).

- `int tri(int n);`

  Returns the `n`th triangular number.  Triangular numbers are, informally

  ```
  1    .
 
       .
  3   . .

       .
      . .
  6  . . .
  ```

  and so on.  More formally, the `n`th triangular number, for `n > 0`, is the
  sum of the integers between `1` and `n`, inclusive.

  Note that there is a closed form expression for finding the `n`th triangular
  number (and a famous story about Gauss coming up with it, as a child); but
  for this assignment, please find the answer algorithmically :-).

### Part 5

Rewrite the functions you wrote in Part 4 as iterative functions (append
`_iter` to your name for the recursive version of the function).

### Challenge

- `std::string int_to_roman(int n);`

  A recursive version of the `int_to_roman()` function from assignment-01

- `std::string int_to_words(int n);`

  A recursive function taking in any integer, `n`, and returning a string
  containing the English representation of that number.  For example, the
  following code:

  ```c++
    cout << 0 << " == " << int_to_words(0) << endl;
    cout << 1 << " == " << int_to_words(1) << endl;
    cout << -1 << " == " << int_to_words(-1) << endl;
    cout << 123 << " == " << int_to_words(123) << endl;
    cout << 123123 << " == " << int_to_words(123123) << endl;
    cout << 123000123 << " == " << int_to_words(123000123) << endl;
    cout << 123123000 << " == " << int_to_words(123123000) << endl;
  ```

  should produce the following output:

  ```
  0 == zero
  1 == one
  -1 == negative one
  123 == one hundred twenty three
  123123 == one hundred twenty three thousand one hundred twenty three
  123000123 == one hundred twenty three million one hundred twenty three
  123123000 == one hundred twenty three million one hundred twenty three thousand
  ```

  While writing this, remember the use of `const` arrays in the in-class
  solution to assignment-01.  A similar technique may save you a lot of `if ...
  else` statements.

  Also, if you find it useful, you may modify the function signature slightly.

  As a general approach to solving this problem, I would recommend starting by
  writing a function that can correctly handle all the numbers from 1--999,
  then extending it to handle all possible numbers by splitting the original
  number into groups of 3 digits, recursively passing these smaller groups
  to itself, and appending the correct suffix (e.g. "thousand") to each group.

- `std::string magic_number(int n);`

  Ponder this:

  ```
  1 is 3
  3 is 5
  5 is 4
  4 is the magic number!

  7 is 5
  5 is 4
  4 is the magic number!

  13 is 8
  8 is 5
  5 is 4
  4 is the magic number!
  ```

  Why is 4 the magic number?  Is 4 always the magic number?

  Once you figure it out, write a recursive function that generates the above
  example given the following:

  ```c++
  cout << magic_number(1) << endl;
  cout << magic_number(7) << endl;
  cout << magic_number(13) << endl;
  ```

## Requests

(None)


## Assumptions

(None)


## Style

- Place your solution in a `solution--YOURNAME` subdirectory
  (where `YOURNAME` is your GitHub username).

- Include your copyright and license information at the top of every file,
  followed by a brief description of the file's contents, e.g.

  ```c++
  /* ----------------------------------------------------------------------------
   * Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
   * Released under the [MIT License] (http://opensource.org/licenses/MIT)
   * ------------------------------------------------------------------------- */

  /**
   * A short program to print "Hello World!" to standard output.
   */
  ```

- Use "include guards" in all `.h` files.  Be sure to give the preprocessor
  variable a name corresponding to the file name.  For example, in `point.h`:

  ```c++
  #ifndef POINT_H
  #define POINT_H
  // ----------------------------------------------------------------------------

  // ... everything besides the copyright information and file description

  // ----------------------------------------------------------------------------
  #endif  // POINT_H
  ```

- `main()` must have its own `.cpp` file.  I suggest calling it `main.cpp`.
- Classes must have both `.h` and `.cpp` files, with member functions defined
  in the `.cpp` files unless they are truly trivial.  If it makes sense, you
  may put multiple classes into one pair of `.h` and `.cpp` files.

- Declare member functions and function arguments as `const` when appropriate
  (in general, whenever possible).

- Document and format your code well and consistently.  Be sure to clearly
  document the source of any code, algorithm, information, etc. that you use or
  reference while completing your work.
- Wrap lines at 79 or 80 columns whenever possible.
- End your file with a blank line.
- Do *not* use `using namespace std;`.  You may get around typing `std::` in
  front of things or with, e.g., `using std::cout;`.


-------------------------------------------------------------------------------
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)]
(http://creativecommons.org/licenses/by/4.0/)  
Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>  
This work is licensed under a [Creative Commons Attribution 4.0 International
License] (http://creativecommons.org/licenses/by/4.0/)  
Project located at <https://github.com/2016-spring-csuf-benblazak-cpsc-121>

