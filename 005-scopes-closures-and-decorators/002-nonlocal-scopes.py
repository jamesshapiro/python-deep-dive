"""
Inner Functions

We can define functions from inside another function:
"""

"""
(Not pictured, built-in scope)
+------------------------------------------------------+
| global (namespace 1)                                 |
|                                                      |
|    +-----------------------------------------+       |
|    | local (outer_func) (namespace 2)        |       |
|    |                                         |       |
|    |    +-----------------------------+      |       |
|    |    | local (inner_func) (ns 3)   |      |       |
|    |    |                             |      |       |
|    |    +-----------------------------+      |       |
|    |                                         |       |
|    +-----------------------------------------+       |
|                                                      |
+------------------------------------------------------+

Both functions have access to the global and built-in scopes as
well as their respective local scopes

But the inner function also has access to its *enclosing* scope
-- the scope of the outer function.

That scope is neither local (to inner_func) nor global, it is
called a *nonlocal* scope
"""

def outer_func():
    # some code

    def inner_func():
        pass

    inner_func()

outer_func()

"""
Recap: When we call outer_func, Python sees the reference to "a"

Since "a" is not in the local scope, Python looks in the *enclosing*
(global) scope.
"""

a = 10
def outer_func():
    print(f'{a=}')

print(f'{outer_func()=}')

"""
Now consider this example:

module_1.py

When we call outer_func, inner_func is created and called

When inner_func is called, Python does not find "a" in the local
(inner_func) scope.

So it looks for it in the *enclosing* scope, in this case the
scope of "outer_func"
"""
def outer_func():
    a = 10

    def inner_func():
        print(f'{a=}')
    
    inner_func()
print()
outer_func()

"""
When we call outer_func, inner_func is defined and called

When inner_func is called, Python does not find "a" in the local
(inner_func) scope, so it looks for it in the *enclosing* scope,
in this case the scope of "outer_func"

Since it does not find it there either, it looks in the enclosing
(global) scope
"""
print()
outer_func()
a = 10
def outer_func():
    def inner_func():
        print(f'{a=}')
    
    inner_func()
print()
outer_func()
"""
Modifying global variables

We saw how to use the global keyword in order to modify a global
variable within a nested scope
"""
a = 10
def outer_func2():
    def inner_func():
        global a
        a = 'hello'    
    inner_func()
print()
outer_func2()
print(f'{a=}')

"""
Modifying nonlocal variables

Can we modify variables defined in the outer nonlocal scope?
"""

"""
When inner_func is compiled, Python sees an assignment to x.
So it determines that x is a local variable to inner_func
The variable x in inner_func masks the variable x in outer_func
"""
def outer_func():
    x = 'hello'
    print(f'{x=}')
    def inner_func():
        x = 'python'
        print(f'{x=}')
    inner_func()
    print(f'{x=}')
print()
outer_func()

"""
Modifying nonlocal variables

Just as with global variables, we have to explicitly tell Python we are
modifying a nonlocal variable
"""

def outer_func():
    x = 'hello'
    print(f'{x=}')
    def inner_func():
        nonlocal x
        x = 'python'
        print(f'{x=}')
    inner_func()
    print(f'{x=}')
print()
outer_func()

"""
Nonlocal Variables

Whenever Python is told that a variable is nonlocal,
    - it will look for it in the *enclosing local scopes* chain until it first
      encounters the specified variable name
    - Beware: It will ONLY look in local scopes, it will *not* look in the global scope
"""

"""
(Not pictured, built-in scope)
+-------------------------------------------------------------------------+
| global (namespace 1)                                                    |
|                                                                         |
|    +------------------------------------------------------------+       |
|    | local (outer_func) (namespace 2)                           |       |
|    |                                                            |       |
|    |                +-----+                                     |       |
|    |                |  x  |                                     |       |
|    |                +-----+                                     |       |
|    |                                                            |       |
|    |    +------------------------------------------------+      |       |
|    |    | local (inner_1) (ns 3)                         |      |       |
|    |    |                                                |      |       |
|    |    |    +----------------------------------+        |      |       |
|    |    |    | local (inner_2) (ns 4)           |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    +----------------------------------+        |      |       |
|    |    |                                                |      |       |
|    |    +------------------------------------------------+      |       |
|    |                                                            |       |
|    +------------------------------------------------------------+       |
|                                                                         |
+-------------------------------------------------------------------------+
"""
def outer_func():
    x = 'hello'
    print(f'{x=}')
    def inner_1():
        def inner_2():
            nonlocal x
            x = 'python'
            print(f'{x=}')
        inner_2()
    inner_1()
    print(f'{x=}')
print()
outer_func()

"""
Nonlocal Variables

But consider this example:

+-------------------------------------------------------------------------+
| global (namespace 1)                                                    |
|                                                                         |
|    +------------------------------------------------------------+       |
|    | local (outer_func) (namespace 2)                           |       |
|    |                                                            |       |
|    |                +-----+                                     |       |
|    |                |  x  |                                     |       |
|    |                +-----+                                     |       |
|    |                                                            |       |
|    |    +------------------------------------------------+      |       |
|    |    | local (inner_1) (ns 3)                         |      |       |
|    |    |                                                |      |       |
|    |    |           +-----+                              |      |       |
|    |    |           |  x  |                              |      |       |
|    |    |           +-----+                              |      |       |
|    |    |                                                |      |       |
|    |    |    +----------------------------------+        |      |       |
|    |    |    | local (inner_2) (ns 4)           |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    +----------------------------------+        |      |       |
|    |    |                                                |      |       |
|    |    +------------------------------------------------+      |       |
|    |                                                            |       |
|    +------------------------------------------------------------+       |
|                                                                         |
+-------------------------------------------------------------------------+
"""
def outer_func():
    x = 'hello'
    print(f'{x=}')
    def inner_1():
        x = 'world'
        print(f'{x=}')
        def inner_2():
            nonlocal x
            x = 'python'
            print(f'{x=}')
        inner_2()
    inner_1()
    print(f'{x=}')
print()
outer_func()

"""
Another example

+-------------------------------------------------------------------------+
| global (namespace 1)                                                    |
|                                                                         |
|    +------------------------------------------------------------+       |
|    | local (outer_func) (namespace 2)                           |       |
|    |                                                            |       |
|    |                +-----+                                     |       |
|    |                |  x  |                                     |       |
|    |                +-----+                                     |       |
|    |                                                            |       |
|    |    +------------------------------------------------+      |       |
|    |    | local (inner_1) (ns 3)                         |      |       |
|    |    |                                                |      |       |
|    |    |    +----------------------------------+        |      |       |
|    |    |    | local (inner_2) (ns 4)           |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    |                                  |        |      |       |
|    |    |    +----------------------------------+        |      |       |
|    |    |                                                |      |       |
|    |    +------------------------------------------------+      |       |
|    |                                                            |       |
|    +------------------------------------------------------------+       |
|                                                                         |
+-------------------------------------------------------------------------+
"""
def outer_func():
    x = 'hello'
    print(f'{x=}')
    def inner_1():
        nonlocal x
        x = 'world'
        print(f'{x=}')
        def inner_2():
            nonlocal x
            x = 'python'
            print(f'{x=}')
        inner_2()
    inner_1()
    print(f'{x=}')
print()
outer_func()

"""
Nonlocal and Global Variables
"""
x = 100
print()
print(f'before outer          -- {x=}')
def outer_func():
    x = 'hello'
    print(f'outer before inner_1  -- {x=}')
    def inner_1():
        nonlocal x
        x = 'world'
        print(f'inner_1               -- {x=}')
        def inner_2():
            global x
            x = 'python'
            print(f'inner_2               -- {x=}')
        inner_2()
        print(f'inner_1 after inner_2 -- {x=}')
    inner_1()
    print(f'outer after inner_1   -- {x=}')

outer_func()
print(f'... after outer       -- {x=}')



#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')