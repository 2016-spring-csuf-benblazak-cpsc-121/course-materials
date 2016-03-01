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

Write as many of the following functions as you can in roughly 3 hours:

- TBA (various recursive functions)
<!-- TODO -->

### Part 5

Rewrite the functions you wrote in Part 4 as iterative functions (append
`_iter` to your name for the recursive version of the function).

### Challenge

- TBA (int to words)
<!-- TODO -->


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

