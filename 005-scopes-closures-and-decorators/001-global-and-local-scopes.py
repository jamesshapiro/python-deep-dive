"""
Scopes and Namespaces

When an object is assigned to a variable: a = 10
  ... that variable points to some object
      and we say that the variable (name) is *bound* to that object

That object can be accessed using that name in various parts of our code

But not just anywhere!

That variable name and its binding (name and object) only "exist"
in specific parts of our code.

- The portion of code where that name/binding is defined is called the
*lexical scope* of the variable.
- These bindings are stored in namespaces
- Each scope has its own namespace
"""

"""
The Global Scope

The global scope is essentially the module scope.

It spans a single file only.

There is no concept of a truly global (across all the modules in our entire app) scope in Python.

The only exception to this are some of the *built-in* globally available objects, such as:
- True
- False
- None
- dict
- print

The built-in and global variables can be used *anywhere* inside our module (including inside of functions)
"""

"""
Global scopes are nested inside the built-in scope

+------------------------------------------------------+
| Built-in Scope (namespace 1)                         |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 1 Scope (namespace 2)            |       |
|    |                                         |       |
|    |                                         |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 2 Scope (namespace 3)            |       |
|    |                                         |       |
|    |                                         |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
+------------------------------------------------------+

namespace 1
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+      var_1       +  0xA345E         +
+      func_1      +  0xFF34A         +
+++++++++++++++++++++++++++++++++++++++

Why nested?

If you reference a variable name inside a scope and Python
*does not find it* in that scope's namespace, then it will
look for it in the *enclosing* scope's namespace
"""

"""
module1.py

print(True)

# Python does not find "True" or "print" in the current
# (module/global) scope.
# So, it looks for them in the enclosing scope -> built-in
# Finds them there
"""

"""
module2.py

print(a)

# Python does not find "print" or "a" in the current
# (module/global) scope.
# So, it looks for them in the enclosing scope -> built-in
# Finds "print" but not "a" there, so throws a NameError
"""
try:
    print(a)
except NameError as e:
    print(e)

"""
module3.py

print = lambda x: f'hello {x}'
s = print('world')

# This will actually overwrite print in the (module/global)
# scope which will prevent it from ever writing to stdout

# In other words, Python finds print in the module scope.
# So it uses it!
# 
# s -> "hello world"
#
# Usually not a good idea to do this
"""

"""
The Local Scope

When we create functions, we can create variable names inside
those functions (using assignments)

Variables defined inside a function are not created until the
function is called

Every time the function is called, a *new scope is created*

Variables defined inside the function are assigned to that scope
 -> Function local scope
 -> Local scope

The actual object the variable references could be *different* 
each time the function is called. This is why recursion works.
"""

var = 1
def local_scope_example():
    var = 2
    print(f'{var=}')

print(f'{var=}')
local_scope_example()

def my_func(a,b):
    c = a * b
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')
    return c

"""
a,b,c are all local to my_func

At compile time when Python encounters this piece of code
it looks at everything in my_func and determines that
a, b, and c are going to be local variables. It doesn't
create the scope or namespace because we haven't called the
function. But it does predetermine that when they are
created, they will be created into a local namespace. NOT
the module or built-in namespace.

These names will be considered *local* to my_func
"""
a = 'global'
b = 'global'
c = 'global'
print(f'{my_func("z",2)=}')
print(f'{a=}')
print(f'{b=}')
print(f'{c=}')
print(f'{my_func(10,5)=}')

"""
Nested Scopes
Scopes are often nested

+------------------------------------------------------+
| Built-in Scope (namespace 1)                         |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 1 Scope (namespace 2)            |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 3)   |      |       |
|    |    |                             |      |       |
|    |    |                             |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 4)   |      |       |
|    |    |                             |      |       |
|    |    |                             |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    +-----------------------------------------+       |
|                                                      |
|                                                      |
+------------------------------------------------------+

Namespace lookups

When requesting the object bound to a variable name:
    e.g. print(a)
Pytohn will try to find the object bound to the variable:
    - in current local scope first
    - works up the chain of enclosing scopes

+------------------------------------------------------+
| Built-in Scope (namespace 1)                         |
|                                                      |
|    +------+                                          |
|    | True |                                          |
|    +------+                                          |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 1 Scope (namespace 2)            |       |
|    |                                         |       |
|    |     +-------+                           |       |
|    |     | a->10 |                           |       |
|    |     +-------+                           |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 3)   |      |       |
|    |    |                             |      |       |
|    |    |    +-------+                |      |       |
|    |    |    | b->20 |                |      |       |
|    |    |    +-------+                |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 3)   |      |       |
|    |    |                             |      |       |
|    |    |    +--------+               |      |       |
|    |    |    | b->'a' |               |      |       |
|    |    |    +--------+               |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
+------------------------------------------------------+
"""
a = 10
def my_func(b):
    print(True)
    print(a)
    print(b)

print()
my_func(20)
print()
my_func('a')
print()

"""
Accessing the global scope from a local scope

When *retrieving* the value of a global variable from inside
a function, Python automatically searches the local scope's
namespace, and up the chain of enclosing namespaces

local -> global -> built-in

What about modifiying a global variable's value from inside the
function?

+------------------------------------------------------+
| Built-in Scope (namespace 1)                         |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 1 Scope (namespace 2)            |       |
|    |                                         |       |
|    |     +------------------------+          |       |
|    |     | a->0, my_func->0x12345 |          |       |
|    |     +------------------------+          |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 3)   |      |       |
|    |    |                             |      |       |
|    |    |    +--------+               |      |       |
|    |    |    | a->100 |               |      |       |
|    |    |    +--------+               |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
+------------------------------------------------------+
"""

a = 0
def my_func():
    # assignment -> Python interprets this as a local variable
    # at compile-time. The local variable "a" masks the global
    # variable "a"
    a = 100
    print(f'{a=}')
my_func()
print(f'{a=}')

"""
The *global* keyword

We can tell Python that a variable is meant to be scoped in the global scope
by using the *global* keyword
"""
print()
a = 0
def my_func():
    global a
    a = 100
    print(f'{a=}')
my_func()
print(f'{a=}')

"""
Global and Local Scoping

When Python encounters a function definition at compile-time
it will scan for any labels (variables) that have values assigned to them
(anywhere in the function). If the label has not been specified as global,
then it will be local.
"""

"""
+------------------------------------------------------+
| Built-in Scope (namespace 1)                         |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 1 Scope (namespace 2)            |       |
|    |                                         |       |
|    |     +------------------------+          |       |
|    |     | a->10                  |          |       |
|    |     +------------------------+          |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 3)   |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
+------------------------------------------------------+
"""
a = 10

# a is referenced only in entire function at compile time
# a is non-local
print()
def func1():
    print(f'{a=}')
func1()
print(f'{a=}')
print()

"""
+------------------------------------------------------+
| Built-in Scope (namespace 1)                         |
|                                                      |
|    +-----------------------------------------+       |
|    | Module 1 Scope (namespace 2)            |       |
|    |                                         |       |
|    |     +------------------------+          |       |
|    |     | a->10                  |          |       |
|    |     +------------------------+          |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | Local Scope (namespace 3)   |      |       |
|    |    |                             |      |       |
|    |    |    +--------+               |      |       |
|    |    |    | a->100 |               |      |       |
|    |    |    +--------+               |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
+------------------------------------------------------+
"""
a = 10
def func2():
    a = 100
    print(f'{a=}')
func2()
print(f'{a=}')
print()

a = 10
def func3():
    global a
    a = 100
    print(f'{a=}')
func3()
print(f'{a=}')
print()

a = 10
def func4():
    try:
        print(a)
    except UnboundLocalError as e:
        print(e)
    a = 100
    print(f'{a=}')
func4()
print(f'{a=}')
print()

a = 10
def my_func(n):
    c = n**2
    return c

def my_func(n):
    print(f'global a: {a=}')
    c = a ** n
    return c

my_func(2)

print(f'{my_func(2)=}')

a = 10
def my_func(n):
    a = 20
    print(f'{a=}')
    c = a ** n
    return c

print()
print(f'{a=}')
my_func(2)
print(f'{a=}')
print()

a = 10
def my_func(n):
    global a
    a = 20
    print(f'{a=}')
    c = a ** n
    return c

print()
print(f'{a=}')
my_func(2)
print(f'{a=}')
print()

def my_func(n):
    global previously_undeclared
    previously_undeclared = 100
    print(f'{previously_undeclared=}')
    c = previously_undeclared ** n
    return c

print()
try:
    print(f'{previously_undeclared=}')
except NameError as e:
    print(e)
print(f'{my_func(2)=}')
print(f'{previously_undeclared=}')
print()

for i in range(10):
    for_loop_var = 'I exist'

print(f'{for_loop_var=}')

