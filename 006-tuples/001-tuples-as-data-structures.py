"""
Tuples vs Lists vs Strings

Tuples
- containers
- order matters
- heterogeneous / homogeneous, but usually heterogeneous
- indexable
- iterable
- immutable
  - fixed length
  - fixed order
  - cannot do in-place sorts
  - cannot do in-place reversals

Lists
- containers
- order matters
- heterogeneous / homogeneous, but usually homogeneous
- indexable
- iterable
- mutable
  - length can change
  - order of elements can change
  - can do in-place sorts
  - can do in-place reversals

Strings
- containers
- order matters
- homogeneous
- indexable
- iterable
- immutable
  - fixed length
  - fixed order
  - cannot do in-place sorts
  - cannot do in-place reversals
"""

"""
Immutability of Tuples
- elements cannot be added or removed
- the order of elements cannot be changed
- works well for representing data structures:
  - Point(10,20)
  - 1st element is the x-coordinate
  - 2nd element is the y-coordinate

  - Circle(10,20,5)
  - 1st element is the x-coordinate of the center
  - 2nd element is the y-coordinate of the center
  - 3rd element is the radius

  - City("London", "UK", 8_780_000)
  - 1st element is the name of the city
  - 2nd element is the country
  - 3rd element is the population

Very lightweight data structure

The position of the data has meaning

Tuples as Data Records

Think of a tuple as a data record where the position of the data has meaning

london = ("London", "UK", 8_780_000)
new_york = ("New York", "USA", 8_500_000)
beijing = ("Beijing", "China", 21_000_000)

Because tuples, strings, and integers are immutable, we are guaranteed
that the data and data structure for london will never change

We can have a list of these tuples

cities = [('London', 'UK', 8_780_000),
          ('New York', 'USA', 8_500_000), 
          ('Beijing', 'China', 21_000_000)]
"""

"""
Extracting data from Tuples

Since tuples are sequences just like strings and lists, we can retrieve items by index
"""

london = ("London", "UK", 8_780_000)
city = london[0]
country = london[1]
population = london[2]

print(city, country, population)

cities = [('London', 'UK', 8_780_000),
          ('New York', 'USA', 8_500_000),
          ('Beijing', 'China', 21_000_000)]

total_population = 0
for city in cities:
    total_population += city[2]

"""
You'll notice how the list of cities is homogeneous (contains cities only)

But a city (the tuple) is heterogeneous
"""

"""
Extracting data from Tuples

We can also use tuple unpacking

We actually already know how to do this -- we covered this in the section on function arguments
"""

new_york = ("New York", "USA", 8_500_000)
# Note: the parentheses aren't actually required
beijing = "Beijing", "China", 21_000_000

city, country, population = new_york
city, country, population = ('New York', 'USA', 8_500_000)
city, country, population = "New York", "USA", 8_500_000

"""
Dummy Variables

This is something you're likely to run across when you look at Python code that uses tuple unpacking

Sometimes, we are only interested in a subset of the data fields in a tuple, not all of them

Suppose we are interested only in the city name and the population
"""

city, _, population = ('Beijing', 'China', 21_000_000)

# Note there is nothing magical about _, it is just the conventional variable name for dummy variables

"""
Dummy variables

These are also used in extended unpacking
"""

record = ('DJIA', 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)
symbol, year, month, day, open_, high, low, close = record

"""
Suppose we are only interested in the symbol, year, month, day, and close fields
"""

symbol, year, month, day, _, _, _, close = record
symbol, year, month, day, *_, close = record

""" CODING SECTION """
a = (10, 20, 30)
b = 10, 20, 30

print(f'{type(a)=}')
print(f'{type(b)=}')

def print_tuple(t):
    for e in t:
        print(e)

print('Note: here we need the parentheses around the tuple to distinguish between the singular tuple and a sequence of function arguments')
print_tuple((10, 20, 30))

a = 'a', 10, 200

print(f'{a[0]=}')
print(f'{a[1]=}')

a = 1,2,3,4,5,6
print(f'{type(a)=}')
print(f'{a[2:5]=}')

for e in a:
    print(e)

a = 'a', 10, 20
x,y,z = a

print(f'{x=}')
print(f'{y=}')
print(f'{z=}')

a = 1,2,3,4,5
x, *_, y, z = a
print(f'{x=}')
print(f'{y=}')
print(f'{z=}')
print(f'{_=}')

try:
    a[0] = 100
except TypeError as e:
    print(e)

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

pt = Point2D(10, 20)
print(f'{pt=}')
print(f'{hex(id(pt))=}')

a = Point2D(x=0,y=0), Point2D(x=10,y=20)

print()
print(f'{hex(id(a[0]))=}')
print(f'{a=}')
a[0].x = 100
print(f'{hex(id(a[0]))=}')
print(f'{a=}')
print()

s = 'python'
print(f'{hex(id(s))=}')
print(f'{s=}')
s = 'python' + 'rocks!'
print(f'{hex(id(s))=}')
print(f'{s=}')

print()
a = 1, 2, 3
print(f'{hex(id(a))=}')
print(f'{a=}')

a += (4, 5)
print(f'{hex(id(a))=}')
print(f'{a=}')

pt1 = (0, 0)
pt2 = (10, 20)

london = ("London", "UK", 8_780_000)
new_york = ("New York", "USA", 8_500_000)
beijing = ("Beijing", "China", 21_000_000)

cities = [london, new_york, beijing]

total = 0
for city in cities:
    total += city[2]
print(f'{total=}')

""" more pythonic """
total = sum(city[2] for city in cities)
print(f'{total=}')

record = ('DJIA', 2018, 1, 19, 25_987, 26_072, 25_943, 26_072)
symbol, year, month, day, open_, high, low, close = record
symbol, *_, close = record

print(f'{symbol=}')
print(f'{close=}')

for city in cities:
    print(f'{city=}')

for city, country, population in cities:
    print(f'{city=}, {country=}, {population=}')

print()
for index, city in enumerate(cities):
    print(f'{index=}, {city=}')

from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)
    if sqrt(random_x**2 + random_y**2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return random_x, random_y, is_in_circle

num_attempts = 100_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately {4*count_inside/num_attempts}')