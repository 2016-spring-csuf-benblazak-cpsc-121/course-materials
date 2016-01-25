# Assignment 01: Roman Numerals
please turn in by 11pm on 2016-02-06

## Requirements

Write a program that

0. Asks the user to enter an integer.
0. Prints the integer in Roman numerals.
0. Asks the user if they'd like to convert another integer.
    - If the user enters `'n'` or `'N'`, end the program.
    - Otherwise, go back to step 1.

- Handle user interaction within `main()`.
- Handle the conversion of an integer into a Roman Numeral in a separate,
  appropriately named function.


## Requests

- Please try to do this in groups, and try to use Google, etc., only for
  answers to questions about the language (as opposed to questions about this
  problem).


## Assumptions

- The user will enter the correct *type* of data when prompted.


## Style

- Place your solution in a `solution--YOURNAME` subdirectory
  (where `YOURNAME` is your GitHub username).

- Document and format your code well and consistently.  Be sure to clearly
  document the source of any code, algorithm, information, etc. that you use or
  reference while completing your work.
- Wrap lines at 79 or 80 columns whenever possible.
- End your file with a blank line.
- Do *not* use `using namespace std;`.  You may get around typing `std::` in
  front of things or with, e.g., `using std::cout;`.

- `main()` must have its own `.cpp` file.  I suggest calling it `main.cpp`.

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


## Sample Run

```
Please enter an integer: 123
--> CXXIII

Would you like to convert another integer (Y/N)? y

Please enter an integer: 401
--> CDI

Would you like to convert another integer (Y/N)? y

Please enter an integer: 1299
--> MCCXCIX

Would you like to convert another integer (Y/N)? n
```


-------------------------------------------------------------------------------
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)]
(http://creativecommons.org/licenses/by/4.0/)  
Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>  
This work is licensed under a [Creative Commons Attribution 4.0 International
License] (http://creativecommons.org/licenses/by/4.0/)  
Project located at <https://github.com/2016-spring-csuf-benblazak-cpsc-121>

