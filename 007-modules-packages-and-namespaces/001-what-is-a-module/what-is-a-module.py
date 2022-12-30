"""
What is a Module?
"""

def func():
    a = 10
    return a

print(f'{func=}')
print(f'{hex(id(func))=}')

print(f'{globals()=}')
print(f'{globals()["func"]=}')
f = globals()["func"]
print(f'{f is func=}')

"""
The namespace is basically a dictionary of symbols

Locals is the same as globals in the global scope.
"""

a = 100
print(f'{locals()=}')
print(f'{locals() is globals()=}')

def func():
    a = 10
    b = 10
    """
    But not in the local scope.
    """
    print(f'{locals()=}')
    print(f'{locals() is globals()=}')

func()

"""
Note: math is a built-in, but fractions is not

fractions is written in Python, while math is written in C and built
into the Python language.
"""
import math
print(f'{math=}')
import fractions
print(f'{fractions=}')

print(f'{globals()=}')
junk = math
print(f'{junk.sqrt(2)=}')
print(f'{junk is math=}')

print(f'{globals()["math"]=}')

mod_math = globals()["math"]

print(f'{mod_math.sqrt(2)=}')
print(f'{type(globals())=}')
print(f'{type(math)=}')
print(f'{type(fractions)=}')
print(f'{hex(id(math))=}')

import math

print(f'{hex(id(math))=}')

"""
There is a global cache that prevents the same module from being
loaded twice (for example from two different files with the same
import statement).
"""

import sys

"""

"""
print(f'{sys.modules["math"]=}')
print(f'{hex(id(sys.modules["math"]))=}')
print(f'{math.__name__=}')
print(f'{math.__dict__=}')

f = math.__dict__["sqrt"]
print(f'{f}')
print(f'{f(2)=}')

import fractions
print(f'{sys.modules["fractions"]=}')
print(f'{dir(fractions)=}')
print(f'{fractions.__dict__=}')

import calendar
print(f'{calendar=}')

"""
So all modules get loaded from a file.

They are a regular data type of type module

They have a namespace.

They basically are a container of global variables.
"""

import types
print(f'{isinstance(fractions, types.ModuleType)=}')
print(f'{isinstance(math, types.ModuleType)=}')

import collections
print(f'{isinstance(collections, types.ModuleType)=}')

"""
We can even create our own module objects
"""
mod = types.ModuleType('test', 'This is a test module')
print(f'{isinstance(mod, types.ModuleType)=}')
print(f'{mod.__dict__=}')

mod.pi = 3.14
print(f'{mod.__dict__=}')

mod.hello = lambda: 'Hello!'
print(f'{mod.hello()=}')

hello = mod.hello
print(f'{"hello" in globals()=}')
print(f'{"mod" in globals()=}')
print(f'{hello()=}')

from collections import namedtuple

mod.Point = namedtuple('Point', 'x y')
p1 = mod.Point(10, 20)
p2 = mod.Point(30, 40)

print(f'{dir(mod)=}')

PT = getattr(mod, 'Point')
example_pt = PT(20, 20)
print(f'{example_pt=}')

PT = mod.__dict__['Point']
example_pt = PT(20, 20)
print(f'{example_pt=}')

