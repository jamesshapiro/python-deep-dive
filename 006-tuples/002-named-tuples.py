"""
Tuple as Data Structure

We have seen how we interpreted tuples as data structures

The **position** of the object contained in the tuple gave it **meaning**

For example, we can represent a 2D coordinate as: (10, 20)

If pt is a position tuple we can retrieve the x and y coordinates using:

x, y = pt

or:

x = pt[0]
y = pt[1]

So, for example, to calculate the distance of pt from the origin, we could write:

dist = math.sqrt(pt[0] ** 2 + pt[1] ** 2)

Which is not clear to the reader who does not know what these indices mean
"""

"""
Using a Class Instead

At this point, in order to make things clearer for the read (not the compiler), we
might want to approach this using a class instead.
"""

import math
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
pt = Point2D(10, 20)
distance = math.sqrt(pt.x ** 2 + pt.y ** 2)

class Stock:
    def __init__(self, symbol, year, month, day, open_, high, low, close):
        self.symbol = symbol
        self.year = year
        self.month = month
        self.day = day
        self.open_ = open_
        self.high = high
        self.low = low
        self.close = close

"""
But this is overkill

Class Approach:
djia.symbol
djia.open
djia.close
djia.high - djia.low

Tuple Approach:
djia[0]
djia[4]
djia[7]
djia[5] - djia[6]

Extra Stuff:
At the very least we should implement the __repr__ method
-> Point(x=10, y=20)

We probably should implement the __eq__ method too
-> Point(x=10, y=20) == Point(x=10, y=20) -> True
"""

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

"""
Named tuples to the rescue

There are other reasons to seek another approach.

Among other things, Point2D objects are **mutable** -- something we may not want!

There's a lot to like using tuples to represent simple data structures

The main drawback is that we have to remember the order of the fields and remember
this in our code

If we ever need to change the structure of our tuple in our code (like inserting a value that we forgot) most likely our code will break
"""
eric = ('Idle', 42)








# ... big gap in your code ...







eric = ('Eric', 'Idle', 42)










# ... big gap in your code ...






# OOPS
try:
    last_name, age = eric
except ValueError as e:
    print(e)


"""
Named Tuples to the rescue

So what if we could somehow combine these two approaches, essentially creating
tuples where we can, in addition, give meaningful names to the positions?

That's what namedtuples essentially do

They subclass tuple, and add a layer to assign **property names** to the **positional** elements

Located in the **collections** standard library module
"""

from collections import namedtuple

"""
namedtuple is a function which generates a new class -> class factory
    - that new class **inherits** from tuple
    - but also provides **named properties** to access elements of the tuple
    - but an instance of the class is still a tuple

Generating Named Tuple Classes

We have to understand that namedtuple is a class factory

When we use it, we are essentially **creating a new class**, just as if we had used class ourselves

namedtuple needs a few things to generate this class:
    - the **class name** we want to use
    - a sequence of **field names (strings)** we want to assign, in the order of the elements of the tuple
        - field names can be any **valid** variable name except that they cannot start with an underscore

The return value of the call to namedtuple will be a class

We need to assign that class to a variable name in our code so we can use it to construct instances

In general, we use the same name as the name of the class that was generated
"""

Point2D = namedtuple('Point2D', ['x', 'y'])

"""
We can create instances of Point2D just as we would with any class (since it is a class)
"""

pt = Point2D(10, 20)

"""
The variable name that we use to assign to the class generated and returned by namedtuple is arbitrary
"""

Pt2D = namedtuple('Point2D', ['x', 'y'])
pt = Pt2D(10, 20)


# Similar to:
class MyClass:
    pass

MyClassAlias = MyClass
instance_1 = MyClass()

#Similarly:

Pt2DAlias = namedtuple('Point2D', ['x', 'y'])

"""
There are many ways we can provide the list of field names to the namedtuple function
- a list of string
- a tuple of strings
- in fact, any sequence, just remember that order matters
- a single string with the field names separated by whitespace or commas
"""

namedtuple('Point2D', ['x', 'y'])
namedtuple('Point2D', ('x', 'y'))
namedtuple('Point2D', 'x, y')
namedtuple('Point2D', 'x y')

"""
Instantiating Named Tuples

After we have created a named tuple class, we can instantiate them just like an ordinary class

In fact, the __new__ method of the generated class uses the field names we provided as param names
"""

Point2D = namedtuple('Point2D', 'x y')

"""
We can use **positional** arguments:
"""
pt1 = Point2D(10, 20)
"""
Or even keyword arguments:
"""
pt2 = Point2D(x=10, y=20)
pt3 = Point2D(y=20, x=10)
print(f'{pt3=}')

"""
Accessing Data in a Named Tuple

Since named tuples are also regular tuples, we can still handle them like any other tuple
- by index
- slice
- iterate
"""
Point2D = namedtuple('Point2D', 'x y')
pt1 = Point2D(10, 20)
print(f'{pt1[0]=}')
print(f'{pt1[1]=}')
print(f'{isinstance(pt1, tuple)=}')
x, y = pt1
x = pt1[0]
y = pt1[1]

for e in pt1:
    print(e)

"""
But now, in addition, we can also access the data using the field names
"""
print(f'{pt1.x=}')
print(f'{pt1.y=}')

"""
Since namedtuples generate classes inherit from tuple, it's the same as doing:

class Point2D(tuple):
    ...

pt1 **is** a tuple, and is therefore **immutable**
"""
try:
    pt1.x = 100
except AttributeError as e:
    print(e)

"""
The **rename** keyword-only argument for namedtuple

Remember that field names for namedtuple must be valid identifiers, and cannot start with an underscore

Hence, this would not work:

Person = namedtuple('Person', 'name age _ssn')

But namedtuple has a keyword-only argument, **rename**, that will automatically rename any invalid field name

uses convention: _{position in list of field names}

This **will** now work:
"""
Person = namedtuple('Person', 'name age _ssn', rename=True)

"""
And the actual field names would be:

name, age, and _2
"""

"""
Introspection:

We can easily find out the field names in a named tuple generated class

class property -> _fields
"""

Person = namedtuple('Person', 'name age _ssn', rename=True)
print(f'{Person._fields=}')

"""
Extracting Named Tuple Values to a Dictionary

Instance method: _asdict()
"""
Point2D = namedtuple('Point2D', 'x y')
pt1 = Point2D(10, 20)

pt1._asdict() # -> {'x': 10, 'y': 20}






