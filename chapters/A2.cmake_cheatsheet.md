#Cmake cheat sheet

## quick start
1. first example, see more details at <https://cmake.org/cmake-tutorial/>

```
cmake_minimum_required (VERSION 2.8.0)#cmake grammar evolves, 
project (testcpp) # define the output executive name

add_executable (testcpp testcpp.cpp) #define source to object relation
```

2. in source build cmdline:  
`cmake <path to toplevel cmakelists.txt> -G <generator> && make` 

out of source build is recommended to keep source tree clean:  
```
cd dir_of_source_with_toplevel_cmakelists.txt && mkdir build 
cd build && camke .. &&make
make install
```

using `nmake` on windows visual studio build tool, as cmake generate platform specific makefile

3. GUI tool `cmake-gui <path to toplevel cmakelists.txt>`
build option can be turn on and off in GUI  
```
option(<option_variable> "help string describing option"
       [initial value])
```
4. FindGTK module, work like `pkg-config` to get include and lib path

```
GTK_INCLUDE_DIR   - Directories to include to use GTK
GTK_LIBRARIES     - Files to link against to use GTK
GTK_FOUND         - GTK was found
GTK_GL_FOUND      - GTK's GL features were found
```
for more details see <https://cmake.org/Wiki/CMake>


## cmake language syntax

cmake is a script language, similar with shell to some extent.
see [cmake wiki](https://cmake.org/Wiki/CMake/Language_Syntax)

+ only one kind of variable, i.e. string,   
> but it will be interpreted as bool in `IF (var)`  
or integer `IF (var GREATER 10) ... ENDIF`

+ variable substitution `${VAR}`, SET and UNSET, `IF(DEFINED x)`

+ only one kind of data structure: LIST, string sperated by semicolon  
`SET(var a b c)` is equal to `SET(var "a;b;c")`

+ quotation mark to reserve sapce "hello world"
```
SET( x a b c   ) # stores a list "a;b;c" in x      (without quotes)
SET( y "a b c" ) # stores a string "a b c" in y      (without quotes)
MESSAGE( a b c ) # prints "abc"   to stdout, automatically concat (without quotes)
MESSAGE( ${x} )  # prints "abc"   to stdout (without quotes)
MESSAGE("${x}")  # prints "a;b;c" to stdout (without quotes)
MESSAGE( ${y} )  # prints "a b c" to stdout (without quotes)
MESSAGE("${y}")  # prints "a b c" to stdout (without quotes)
```
+ comment by #, escape by \, line continuation by /
> but in path string: "http://////www.example.com"

> but it is different from bash shell

> newline to split list element

- cmake variable and command is case insensitive  
> but UPPER case for command is recommended   
and variable content like filename is case sensitive

- ""(empty string), "NO; N; FALSE; <var>-NOTFOUND; OFF;0;" or lower case is regarded false in IF()

- only integer algorithm `MATH(EXPR outputvar expr)`  
```
SET( expression 4 LESS 10 ) # ${expression} is now "4;LESS;10"
IF( ${expression} )         # expands to IF( 4;LESS;10 )
  MESSAGE( "CMake believes that 4 is less than 10." )
ENDIF( ${expression} )
```
bash shell math: `$((math_expr))` 

- generate `config.h` from `config.h.cmake` template   
> by replacing "@var" with var defined in camkelists.txt
`MESSAGE( ${x}${y} ) # displays "31"`

- function is different from macro whose variables have global scope

## important commands and variables
see more details on variable at <https://cmake.org/Wiki/CMake_Useful_Variables>

### 1.commands

+ $ENV{HOME} #access to environment variable
+ EXECUTE_PROCESS(cmd var_to_hold_result)
+ INSTALL(TARGETS|FILES list_of_f dest)
+ CONFIGURE_FILE() #generate config.h from config template input file
+ INCLUDE_DIRECTORY() #subdir with cmakelists.txt
+ ADD_LIBRARY(), ADD_EXECUTABLE(), add_definitions, add_dependencies
+ INCLUDE(extra_cmake_file) #as include in c++ for extra functions

### 2. location variables

+ SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/MyCMakeScripts) 
> where FIND_PACKAGE(FooBar) can find `findFooBar.cmake`

+ CMAKE_SOURCE_DIR # top source dir containing the top-level CMakeLists.txt,
+ CMAKE_BINARY_DIR # top folder to build binary object
+ CMAKE_CURRENT_LIST_FILE # full path of the current processed cmakelists.txt
+ CMAKE_INCLUDE_PATH  # path to search for header file e.g. `/usr/include`
+ CMAKE_INSTALL_PREFIX #just as DESTDIR in `make DESTDIR=/home/john install`

### 3. compiler control variables
+ CMAKE_CXX_COMPILER 
+ CMAKE_BUILD_TYPE # NONE, DEBUG, RELEASE, etc
+ CMAKE_<Lang>_FLAGS # for build_type NONE
+ CMAKE_LINK_LIBRARY_CFLAGS
+ enable C++ standard support in a portable way
```
set(CMAKE_CXX_STANDARD 11) #98, 14, 17
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```

### 4. predefined platform and compiler detection variables   
platform like: WIN32, APPLE, UNIX (linux is UNIX but not APPLE), MYSYS, CYGWIN
compilers: MSVC, MINGW, iNTEL; CMAKE_COMPILER_IS_GNUCXX, CLANG

### 5. command line help
```bash
cmake --variable-list
cmake --command-list
cmake --module-list
cmake -h #show all generator
```

<https://cmake.org/Wiki/CMake_Useful_Variables>

## Why cmake?

cmake is a new language, why should we learn a new language instead of json or python (as in scons)?

1. cmake inherits some conception of traditional unix makefile

2. multiple programming lang support and cross-platform with generators for majourity of IDE tools

3. plenty of official modules like "FindXXX.cmake"

4. speedup by var cache `SET(var value CACHE)`

5. CPACK for binary package and windows NSIS installer generation

6. Generating Dependency Graphs with CMake, `cmake --graphviz=test.dot .`

7. tool to generate cmakelists.txt from scratch or convert from existent build system

## what I do not like

- cmake is not a precise or clear script lang
- confusing string quotation and substitution
- un-intuitive function style programming to c/python programmers
- messed up of variable_content and variable
- mixed up argument list and keyword in function call, not sep by comma
> relies heavily on this function to parse function/command input arg
`CMAKE_PARSE_ARGUMENTS(<prefix> <options> <one_value_keywords> <multi_value_keywords> args...)` 
