- general knowledge :: object-oriented programming
    - Same as on the midterm.

- general programming :: searching, sorting, and algorithm analysis
- design :: pseudocode
    - Same as on the midterm.

- design :: documentation
- design :: consistency of style
    - Must be added to one of the other standards where you have to write a
      decent amount of code.

-------------------------------------------------------------------------------

- design :: debugging and testing correctness
    - Know about variable scope, especially as related to for loops.
    - Know the difference between declaring, initializing, and setting
      (changing the value of) a variable.

-------------------------------------------------------------------------------

- review :: data types and representation
    - Know the common fundamental data types, and their typical sizes (in
      bytes, as given by `sizeof`) on a typical 64 bit system.

- review :: arrays
    - Practice filling in memory given a code segment declaring and mutating
      arrays.

- review :: control flow
    - Practice nested for loops for generating different shapes, and putting
      things at the beginning and end of each line.

- review :: operators
    - Practice operator precedence.

- review :: functions
    - Know how to
        - prototype and declare functions separately
        - pass by value, pass by pointer, and pass by reference
        - return values from functions
        - use values returned by functions
        - overload functions
        - use default arguments

-------------------------------------------------------------------------------

- general programming :: recursion
    - Practice short recursive functions:
        - calculate the greatest common divisor of two numbers
        - find the nth fibonacci number
        - raise a number to a positive integer power
        - sum the numbers from 1 to n
        - sum the even numbers from 1 to n
        - sum the odd numbers from 1 to n

- general programming :: type declarations
    - Reference: <http://cdecl.org>
    - Be able to translate between English and C type declarations.
    - Especially know about arrays, references, pointers, function pointers,
      and combinations thereof.

- general programming :: pointers and references
    - Practicing using pointers and references, both alone and as function
      arguments.
    - Know what's happening in memory when pointers and references are used,
      both alone and as function arguments.
    - Know the similarities and differences between pointers and arrays, and
      how to use both.

- general programming :: memory management and dynamic memory
    - Practice dynamic memory allocation.
    - Know the difference between the stack and the heap (or free store).
    - Know what you need to watch out for when dynamically allocating memory.

- general programming :: templates
    - Practice creating and using function templates.
    - Practice creating and using class templates.
    - Practice defining class template methods outside the class.

- general programming :: standard library
    - For `vector`s, and at least one other STL container, know
        - static initialization
        - at least two of the container's methods
        - how to iterate over items in the container
    - For `vector`s, know how to use the `size` and `push_back` methods, and
      the subscript operator (`operator[]`).

-------------------------------------------------------------------------------

- object-oriented programming :: classes
    - Practice
        - constructors
        - destructors
        - initialization lists
        - access specifiers
        - getters and setters
        - using the `this` pointer
        - declaring data members, and initializing them (know how to initialize
          them both inside and outside the class)
        - defining function members inline (inside the class)
        - prototyping function members inside the class, and defining them
          outside the class
        - accessing data members and function members through objects and
          pointers to objects

- object-oriented programming :: exceptions
    - Practice using `throw` in one function or method, and `try ... catch` in
      another.

- object-oriented programming :: interfaces
    - Practice defining interfaces, including
        - a virtual destructor
        - pure virtual methods
    - Practice inheriting from and overriding (at least) all the pure virtual
      methods of an interface.
    - Be familiar with the phrases "abstract base class" and "concrete
      subclass".

- object-oriented programming :: inheritance
    - Practice defining classes that inherit from another class.
        - Note that an access specifier placed before a superclass in the
          "inheritance list" has a different meaning than the same access
          specifier used within the definition of the class.
    - Practice overriding inherited methods.
    - Practice calling the superclass constructor in the initialization list.

- object-oriented programming :: polymorphism
    - Practice tracing through the different behaviors of virtual and non
      virtual methods.

