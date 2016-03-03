# Assignment 04: Searching, Sorting, and Algorithm Analysis
please turn in by 11pm on 2016-03-26

## Requirements

You are allowed to write everything in one file this time, so long it is
organized and the file is not too long.  If the file gets too long, please
split it into multiple `.h` and `.cpp` files, and have a `main.cpp` that
`#include`s the `.h` files, and can be used to call the functions prototyped in
them.

All the files you produce must be able to exist within a single project.  You
will submit these files via github as normal.


### Setup

- Write a function named `print_vector` that takes a `const std::vector<int> &`
  as an argument, and outputs the contents (separated by whitespace) to stdout
  (followed by a newline).

- Write the `main` function.  It doesn't need to do anything right now, but as
  you write the functions below, you should put code in `main` to test them.

### Selection Sort

Write a function named `selection_sort` that takes a `std::vector<int> &` as an
argument, and sorts it in-place.  The algorithm is as follows:

0. For the index of each element in the array (the "current index")

  0. Find the index of the minimum element at or after the current index.
  0. Swap the element at the current index with the smallest element found.

For a more thorough explanation, google around, or see [the relevant Wikipedia
entry](https://en.wikipedia.org/wiki/Selection_sort).

### Merge Sort

Write a function named `merge_sort` that takes as an argument a `const
std::vector<int> &` and returns a `std::vector<int>` containing all the
elements of the vector that was passed as an argument, in ascending order.  The
algorithm (which is recursive) is as follows:

0. If the vector contains only 1 element, return the vector unchanged.
0. Otherwise, split the vector into two halves, named `left` and `right`.
0. Recursively sort each half (i.e. call `merge_sort(left);` and
   `merge_sort(right);`).
0. Merge `left` and `right` into a new vector named `sorted`, in the
   following manner:

    0. As long as `left` and `right` both have elements not in `sorted`,
       compare the smallest such elements of each list, take the
       smaller of the two, and append it to `sorted`.
    0. Once all of the elements of either `left` or `right` are in `sorted`,
       take the leftover elements and append them to `sorted`.

0. Return `sorted`.

For a more thorough explanation, google around, or see [the relevant
Wikipedia entry](https://en.wikipedia.org/wiki/Merge_sort).

You may need to search around for the best way to split a vector into two
smaller vectors.  Here's [one way](http://stackoverflow.com/a/9811343) from
stackoverflow.


## Requests

- Please try to do this in groups, and try to use Google, etc., only for
  answers to questions about the language (as opposed to questions about this
  problem).


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

