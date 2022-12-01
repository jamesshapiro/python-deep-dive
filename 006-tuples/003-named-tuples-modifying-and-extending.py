""" Named Tuples are Immutable

So how can we "change" one or more of the values inside the tuple?

Just like with strings, we have to create a *new* tuple with the modified values
"""
from collections import namedtuple

Point2D = namedtuple('Point', 'x y')
pt = Point2D(0, 0)

"""
Suppose we need to change the value of the x-coordinate:

Simple approach:
"""
pt = Point2D(100, pt.y)

"""
Note that the memory address of pt has now changed
"""

"""
Drawback

This simple approach can work well, but it has a major drawback
"""
Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

"""
Suppose we only want to change the close field

Painful!
"""
djia = Stock(djia.symbol, 
             djia.year, 
             djia.month, 
             djia.day, 
             djia.open, 
             djia.high, 
             djia.low, 
             26_394)

current = djia[:7]
*current, _ = djia

djia = Stock(*current, 26_394)

"""
We can also use the _make class method -- but we need to create an iterable that
contains all the values first:
"""
print(f'{current = }')
new_values = tuple(current) + (26_394,)
#current.append(26_394)

djia = Stock._make(new_values)

"""
But what if we want to change a value in the middle, say, "day"?

Cannot use extended unpacking (only one starred value is allowed in extended unpacking)

This makes no sense...

*pre, day, *post = djia

Because Python doesn't know where to stop *pre and where to start *post

Slicing will work:
"""
pre = djia[:3]
post = djia[4:]
new_values = pre + (26,) + post
djia = Stock._make(new_values)

"""
But even this still has drawbacks:

How about modifying both the *day* and the *high* values?
"""

new_values = djia[:3] + (26,) + djia[4:5] + (26<459,) + djia[6:]
djia = Stock(*new_values)

"""
This is just unreadable and extremely error-prone!

There must be a better way...

There is!

The _replace instance method

Named tuples have a very hany instance method called _replace

It will copy the named tuple into a new one, replacing any values from keyword arguments

The keyword arguments are simply the field names in the tuple and the new values

The keyword name must match an existing field name
"""

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
djia = djia._replace(day=26, high=26_459, close=26_394)
print(f'{djia=}')

"""
Extending a Named Tuple

Sometimes we want to create a named tuple that extends another named tuple,
appending one or more fields
"""

Stock = namedtuple('Stock', 'symbol year month day open high low close')

"""
We want to create a new named tuple class, StockExt, that adds a single field,
previous_close

When dealing with classes, this is sometimes done by using subclassing

But this is not easy to do with named tuples and there's a cleaner way of doing it anyway
"""

"""
Extending a Named Tuple
"""
Point2D = namedtuple('Point', 'x y')

"""
Let's say we want to create a Point3D named tuple that has an extra parameter

Yes, the obvious, and simplest approach here is best:
"""
Point3D = namedtuple('Point3D', 'x y z')

"""
But what happens if you have a lot of fields in the named tuple? 
Code is not as clean anymore...
"""

Stock = namedtuple('Stock', 'symbol year month day open high low close')
StockExt = namedtuple('StockExt', 'symbol year month day open high low close previous_close')

"""
How about re-using the existing field names in Stock?
"""

Stock = namedtuple('Stock', 'symbol year month day open high low close')
print(f'{Stock._fields=}')
new_fields = Stock._fields + ('previous_close',)
print(f'{new_fields=}')
StockExt = namedtuple('StockExt', new_fields)

"""
Extending a Named Tuple

We can also easily use an existing Stock instance to create a new StockExt instance
with the same common values, adding in our new previous_close value:
"""
Stock = namedtuple('Stock', 'symbol year month day open high low close')
StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
djia_ext = StockExt(*djia, 26_000)

"""
or
"""
djia_ext = StockExt._make(djia + (26_000,))

"""CODING SECTION"""

"""
Named Tuples -- Modifying and Extending
"""
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(f'{hex(id(djia))=}')
djia = djia._replace(year=2019, open=10_000)
print(f'{hex(id(djia))=}')