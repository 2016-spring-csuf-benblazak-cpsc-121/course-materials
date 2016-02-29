# Assignment 02: Parable Of the Polygons
please turn in by 11pm on 2016-02-27

- This project is based on a "playable post" by Vi Hart and Nicky Case called
  [Parable of the Polygons](http://ncase.me/polygons/), illustrating the
  effects of bias on population segregation.

- The goal of this project is to get some practice with multiple file projects,
  pointers, and (above all) beginning to intermediate level classes.


**This project may take a lot of time.  Please plan accordingly.  Also, this
project may contain wording you are not yet used to.  Please be patient while
working out what it means, as feel free to ask me if you need help.**


## Requirements

### Week 1

Fill in the `TODO`s (to-do's) in
[buffer.cpp](partial-solution/buffer.cpp)
so that the test function `test_buffer()` in
[main.cpp](partial-solution/main.cpp)
runs and produces the output
```
--------------------------------------------------------------------------------
|                                                                              |
|                                                                              |
|                                      * *                                     |
|                                                                              |
|                                  *         *                                 |
|                                                                              |
|                                                                              |
|                                                                              |
|                                *             *                               |
|                                                                              |
|                                *             *                               |
|                                                                              |
|                                                                              |
|                                                                              |
|                                  *         *                                 |
|                                                                              |
|                                      * *                                     |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
--------------------------------------------------------------------------------
```

Fill in the `TODO`s (to-do's) in
[shape.cpp](partial-solution/shape.cpp)
so that the test function `test_shape()` in
[main.cpp](partial-solution/main.cpp)
runs and produces the output
```
  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.
 / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   |
/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'
.---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  
|   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ 
'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\
  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.
 / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   |
/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'
.---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  
|   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ 
'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\
  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.
 / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   |
/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'
.---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  
|   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ 
'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\
  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.
 / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   |
/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'
.---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  .---.  ,  
|   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ |   | / \ 
'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\'---'/___\
```

Any functions that are not necessary for these tests to run may be "stubbed
out" -- that is, filled in just enough for the program to compile and run,
without being fully implemented.

### Weeks 2 and 3

Fill in the `TODO`s (to-do's) in
[neighborhood.cpp](partial-solution/neighborhood.cpp),
and any remaining uncompleted code in
[buffer.cpp](partial-solution/buffer.cpp) and
[shape.cpp](partial-solution/shape.cpp),
so that the code
```c++
// animate  neighborhood
unsigned int size_x = TERM_SIZE_X/Shape::size_x;
unsigned int size_y = TERM_SIZE_Y/Shape::size_y;
Neighborhood(size_x, size_y).animate(1000);
```
in [main.cpp](partial-solution/main.cpp) runs and produces the output shown in
[demo.mp4](demo.mp4).


## Requests

- Please try to do this in groups, and try to use Google, etc., only for
  answers to questions about the language (as opposed to questions about this
  problem).

- If you have time, you might want to rewrite your solution from scratch,
  referencing your first solution (or mine, if you wish) as little as possible
  (but as much as necessary).  I would recommend doing this not only if you
  have time before the next assignment, but also if you're able to complete the
  next assignment early.


## Assumptions

- A terminal window is 80 columns wide by 25 lines high.


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

