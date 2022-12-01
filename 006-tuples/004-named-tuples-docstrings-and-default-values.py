"""
Default Docs for Named Tuples

When we create a named tuple class, default docstrings are created
"""
from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')
print(f'{Point2D.__doc__=}')
print(f'{Point2D.x.__doc__=}')

"""
The namedtuple function does not provide us a way to define default values for each field

Two approaches to this:

(1.) Using a Prototype
- Create an instance of the named tuple with default values -- the prototype
- Create any additional instances of the named tuple using the prototpye._replace() method

You will need ot supply a default for every field (can be None)

(2.) Using the __defaults__ property

Directly set the defaults of the named tuple constructor (the __new__ method)

You do not need to specify a default for every field

Remember that you cannot have non-defaulted parameters after the first defaulted parameter
"""

# this is fine
def func(a, b=10, c=20):
    print(f'{a=}, {b=}, {c=}')

# this is not fine
# def func(a, b=10, c)

"""
Using a Prototype
"""

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
vector_zero = Vector2D(x1=0, y1=0, x2=0, y2=0, origin_x=0, origin_y=0)
# alternatively
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)

"""
To construct a new instance of Vector2D we now use vector_zero._replace() instead:
"""
vector_one = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)

"""
Using __defaults__
"""

def func(a, b=10, c=20):
    print(f'{a=}, {b=}, {c=}')

print(f'{func.__defaults__=}')

"""
The __defaults__ property is writable

So we can set it to a tuple of our choice

Just don't provide more defaults than parameters! (extras are ignored)

We need to provide defaults to the constructor of our named tuple class
"""

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
Vector2D.__new__.__defaults__ =                      (0, 0)

v1 = Vector2D(10, 10, 20, 20)
print(f'{v1=}')
v2 = Vector2D(10, 10, 20, 20, 100, 100)
print(f'{v2=}')

""" CODING """

Point2D = namedtuple('Point2D', 'x y')
Point2D.__doc__ = 'Represents a 2D Cartesian coordinate'
Point2D.x.__doc__ = 'x-coordinate'
Point2D.y.__doc__ = 'y-coordinate'
print(f'{Point2D.__doc__=}')

