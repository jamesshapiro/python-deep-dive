"""
Decorators

Recall the simple closure example we did which allowed us to maintain a count of
how many times a function was called:

We essentially modified our add function by wrapping it inside another function
that added some functionality to it.

We also say that we decorated our function *add* with the function *counter*.

We wrapped it inside another function.

And we call counter a **decorator** function
"""

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} was called {count} times')
        return fn(*args, **kwargs)
    return inner

def add(a, b=0):
    return a + b

add = counter(add)

print(f'{add(1,2)=}')

"""
Decorators

In general a decorator function:
- takes a function as an argument
- returns a closure
- the closure usually accepts any combination of parameters
- runs some code in the inner function (closure)
- runs some outer code as well
- the closure function calls the original function using the arguments passed to the closure
- returns whatever is returned by that function call

+-------------------------------------------------------------------------+
| outer function (fn)                                                     |
|                                                                         |
|    +------------------------------------------------------------+       |
|    | inner function  (*args, **kwargs)                          |       |
|    |                                                            |       |
|    |     does something                                         |       |
|    |                                                            |       |
|    | returns fn                                                 |       |
|    +------------------------------------------------------------+       |
|                                                                         |
+-------------------------------------------------------------------------+
"""

"""
Decorators and the @ Symbol

In our previous example, we saw that counter was a decorator and we could
decorate our add function using:

    add = counter(add)

In general, if func is a decorator function, we decorate another function
my_func using:

my_func = func(my_func)

But this is so common, that Python provides a convenient way of writing that:
"""
@counter
def mult(a,b):
    return a * b

print(f'{mult(2,3)=}')

"""
This is THE SAME as writing:

def mult(a,b):
    return a * b
mult = counter(mult)

In general:

@func
def my_func(...):
    ...

is the same as writing:

def my_func(...):
    ...

my_func = func(my_func)
"""

"""
Introspecting Decorated Functions

Let's use the same counter decorator
"""
@counter
def mult(a,b,c=1):
    """
        returns the product of three values
    """
    return a * b * c

"""
Remember, we could equally have written:
mult = counter(mult)
"""
"""
- "inner" !!!
- not "mult" !!!
- mult's name "changed" when we decorated it, they are not the same function after all
"""
print(f'{mult.__name__=}')
"""
help(mult) -> Help on funciton inner in module __main__:
    inner(*args, **kwargs)

We have also "lost" our docstring and even the original function signature

Even using the inspect module's signature does not yield better results
"""

"""
One approach to fixing this

We could try to fix this problem, at least for the docstring and function name as follows:
"""
def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} was called {count} times')
        return fn(*args,**kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

"""
But this doesn't fix losing the function signature -- doing so would be quite
complicated.

Instead, Python provides us with a special function that we can use to fix this:

The functools.wraps function

The functools module has a wraps function that we can use to fix the metadata
of our inner function in our decorator

from functools import wraps

In fact, the wraps function is itself a decorator
    but it needs to know what was our "original" function -- in this case fn
"""
from functools import wraps

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner

"""OR, easier to understand"""
def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

@counter
def mult(a: int, b: int, c: int=1):
    """
        returns the product of three values
    """
    return a * b * c

"""
help(mult) ->

Help on function  mutl in module __main__:
   mult(a: int, b: int, c:int=1)
      returns the product of three values

And introspection using the inspect module works as expected:
"""
import inspect
print(f'{inspect.signature(mult)=}')
"""
You don't have to use @wraps, but it will make debugging easier!

It's a good thing to do for other who might use your decorator,
a best practice
"""

"""
CODING SECTION

Decorators -- Part 1
"""

def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        """
        This is the inner closure
        """
        nonlocal count
        count += 1
        print('Note: address of function is the original address of add, not address of the closure')
        print(f'Function {fn.__name__} (id={hex(id(fn))}) was called {count} times')
        return fn(*args, **kwargs)
    
    return inner

def add(a: int, b:int = 0):
    """
    adds two values
    """
    return a + b

print()
print(f'original address of add: {hex(id(add))=}')

add = counter(add)
print(f'new address of closure:  {hex(id(add))=}')

print(f'{add(1,100)=}')
print(f'{add(2,200)=}')

"""
Example of the utility of using *args and **kwargs in your decorator:
More flexibility for the number and variety of arguments you can use
in your decorated function
"""

def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

print(f'{mult(1,2,3,d=4)=}')
print(f'{mult(1,2,d=3)=}')

mult = counter(mult)
print(f'{mult(1,2,3,d=4)=}')
print(f'{mult(1,2,d=3)=}')

"""
@ syntax
"""

@counter
def my_func(s: str, i: int) -> str:
    return s * i

print(f'{my_func("hello", 3)=}')
print(f'{my_func("world", 5)=}')

"""
Restoring original function information (e.g. docstring, name, etc.)
"""

from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        """
        This is the inner closure
        """
        nonlocal count
        count += 1
        print('Note: address of function is the original address of add, not address of the closure')
        print(f'Function {fn.__name__} (id={hex(id(fn))}) was called {count} times')
        return fn(*args, **kwargs)
    
    return inner

@counter
def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

"""
metadata is now correct
"""
import inspect
print(f'{inspect.signature(mult)=}')
