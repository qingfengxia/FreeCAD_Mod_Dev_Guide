# Some common pitfalls for c++

### constness of pointer, a beginner's pitfall

[What is the difference between `const int*, const int * const, and int const *`] (http://stackoverflow.com/questions/1143262/what-is-the-difference-between-const-int-const-int-const-and-int-const)

the key is **read it backward**

```
    int* - pointer to int
    int const * - pointer to const int
    int * const - const pointer to int
    int const * const - const pointer to const int
//Now the first const can be on either side of the type so:
    const int * == int const *
    const int * const == int const * const
```

If you want to go really crazy you can do things like this:

```
    int ** - pointer to pointer to int
    int ** const - a const pointer to a pointer to an int
    int * const * - a pointer to a const pointer to an int
    int const ** - a pointer to a pointer to a const int
    int * const * const - a const pointer to a const pointer to an int
```

### mixed up of unsigned and signed integer

do you understand why Java and Python does not support unsigned integer?, and  what is problem of the following code?

```
void std_container_test(){
    std::vector<int> v;
    int i = 10;
    if (i < v.size()-1) // there is a compiler warning here
        std::cout <<"underflow occurs for empty container size()-1\n";
}

void bool_implicit_coversion_pitfall_test() {
    int x = 0;
    if (!(-0.5 <= x <= 0.5))
        std::cout << "x=0, -0.5 <= x <= 0.5 is false"<<"\n";
} 

```

see full text at <http://www.iesensor.com/blog/2016/12/21/c-and-cpp-pitfal…licit-conversion/>

### trivial constructor

A trivial ctor/destructor is a destructor that performs no action but alloc/delete memory, using default (compiler) generated ctor/dtor()

trivial class: If T is TrivialType (that is, a scalar type, a trivially copyable class with a trivial default constructor, or array of such type/class, possibly cv-qualified)
`std::is_trivial<T>()`

benefit of trivial class:

+ Compiling a trivial class in C++ gives you the same memory layout as a struct compiled in C (Standard-layout )
+ A trivial class (support static initialization) is a class that has a trivial default constructor  is trivially copyable. trivially copyable (a superset of trivial classes), it is ok to copy its representation over the place with things like memcpy and expect the result to be the same.

The standard library has traits to test these properties in the header

```

#include <type_traits>

template <typename T>
struct std::is_pod;
template <typename T>
struct std::is_trivial;
template <typename T>
struct std::is_trivially_copyable;
template <typename T>
struct std::is_standard_layout;

```

### virtual destructor

Virtual functions do not work in constructors.
constructor init member in declear sequence, while destructing in the reverse seq.

> "A common guideline is that a destructor for a base class must be either public and virtual or protected and nonvirtual"

destructors virtual for base class is meant to be manipulated polymorphically, otherwise memory leaks in derived class.

pure virtual function is a virtual function whose declarator has the following syntax as there is no such keyword of pure:`declarator virt-specifier(optional) = 0`, becareful, it is not empty body as {}. It is useful to define *abstract* class. 
