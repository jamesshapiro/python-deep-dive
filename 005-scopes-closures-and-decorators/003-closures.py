"""
Free Variables and Closures

Remember: Functions defined inside another function can access the
outer (nonlocal) variables
"""

def outer():
    x = 'python'

    # This x refers to the one in outer's scope
    # this nonlocal variable x is called a *free* variable
    #
    # When we consider inner, we really are looking at:
    #    - the function inner
    #    - the free variable x (with current value python)
    #
    # This is called a *closure*
    def inner():
        print(f'{x} rocks!')
    
    inner()

#outer()

"""
Returning the inner function

What happens if, instead of calling (running) inner from
inside outer, we return it?
"""

def outer():
    x = 'python'
    # x is a free variable in inner
    # it is bound to the variable x in outer
    # and this happens when outer runs (i.e. when inner is created)
    # this is the closure
    def inner():
        print(f'{x} rocks!')
    return inner

# We can assign that return value to a variable name

fn = outer()
fn()

"""
When we called fn, at that time Python determined the value of x
in the extended scope.

BUT notice that outer had finished running before we called fn.
Its scope was "gone"
"""

"""
Python Cells and Multi-Scoped Variables

Here the vlaue of x is *shared* between two scopes:
    - outer
    - closure
The label x is *in two different scopes*, but always references the same value

Python does this by creating a *cell* as an intermediary object

                    +-------------------------+       +-------------------------+
outer.x ----|       | cell             0xA500 |       | str              0xFF10 |       
            |       |                         |       |                         |       
            |-----> |          0xFF100  ----- | ----> |           "python"      |
            |       |                         |       |                         |       
inner.x ----|       |                         |       |                         |       
                    +-------------------------+       +-------------------------+       

Key:
    "0xA500" memory address of the cell itself
    "0xFF100" reference to another object

In effect, both variables x (in outer and inner), point to the same *cell*

When requesting the value of the variable, Python will "double-hop"
to get to the final value

"""
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

"""
Closures

You can think of the closure as:
    - a function, plus
    - an extended scope that contains the *free variables*

The free variable's value is the object the cell points
to -- so that could change over time.

Every time the function in the closure is called
and the free variable is referenced:

Python looks up the *cell* object, and then whatever the cell
is pointing to
"""
def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10 # local variable
        print(f'{x} rocks!')
    return inner

fn = outer() # fn -> inner + extended scope (x)

"""
Introspection
"""
def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10 # local variable
        print(f'{x} rocks!')
    return inner

fn = outer()
# tuple with all of the free variable labels
print(f'{fn.__code__.co_freevars=}')
# tuple with all of the cells
print(f'{fn.__closure__=}')

# also does the double hop to look up the object id
# of the object referred to by the cell.
def outer():
    x = 'python'
    print(f'{hex(id(x))=}')
    def inner():
        print(f'{hex(id(x))=}')
        a = 10 # local variable
        print(f'{x} rocks!')
    return inner

print()
fn = outer()
fn()
print(f'{fn.__code__.co_freevars=}')
print(f'{fn.__closure__=}')

"""
Modifying free variables
"""
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

counter_1 = counter()
counter_2 = counter()

print(f'{counter_1()=}')
print(f'{counter_1()=}')
print(f'{counter_1()=}')
print(f'{counter_2()=}')
print(f'{counter_2()=}')
print(f'{counter_2()=}')

"""
Multiple Instances of Closures

Every time we run a function, a new scope is created.
"""