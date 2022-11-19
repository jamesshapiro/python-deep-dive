"""
Decorator Application - Decorating Classes
"""
from fractions import Fraction

f = Fraction(2, 3)

print(f'{f.denominator=}')
print(f'{f.numerator=}')

try:
    print(f'{f.speak()=}')
except AttributeError as e:
    print(f'{e=}')

"""
Monkey patching examples
"""

Fraction.speak = 100

print(f'{f.speak=}')

Fraction.speak = lambda self, message: f'Fraction says: {message}'

print(f'{f.speak("This is a late parrot!")=}')

f2 = Fraction(3, 4)

print(f'{f2.speak("This is parrot is no more.")=}')

Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2, 3)
f2 = Fraction(8, 1)

print(f'{f1.is_integral()=}')
print(f'{f2.is_integral()=}')

def dec_speak(cls):
    cls.speak = lambda self, message: f'{cls.__name__} says: {message}'
    return cls

Fraction = dec_speak(Fraction)

f1 = Fraction(2, 3)
print()
print(f'{f1.speak("Hello!")=}')

class Person:
    pass

Person = dec_speak(Person)

p = Person()
print(f'{p.speak("this works!")=}')

print()

from datetime import datetime, timezone

def info(self):
    results = []
    results.append(f'time: {datetime.now(timezone.utc)}')
    results.append(f'Class: {self.__class__.__name__}')
    results.append(f'id: {hex(id(self))}')
    for k,v in vars(self).items():
        results.append(f'{k}: {v}')
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi():
        return 'Hello there!'

p = Person('John', 1939)
print(f'{p.debug()=}')

del Person
del p

def debug_info(cls):
    cls.debug = info

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi():
        return 'Hello there!'

try:
    p = Person('John', 1939)
    print(f'{p.debug()=}')
except TypeError as e:
    print(f'{e=}')

print('the shorthand does not work unless debug_info returns the class')

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi():
        return 'Hello there!'

p = Person('John', 1939)
print(f'{p.debug()=}')

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed')
        self._speed = new_speed

favorite = Automobile('Rolls Royce', 'Black Badge Ghost', 2022, 155)

print(f'\n{favorite.debug()=}')

try:
    favorite.speed = 200
except ValueError as e:
    print(f'{e=}')

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print()
print(f'{abs(p1)=}')
print(f'{p1=}')
print(f'{p1 is p2=}')
print(f'{p2 is p3=}')
print(f'{p1 == p2=}')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)
print()
print(f'{p1 is p2=}')
print(f'{p1 == p2=}')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)
p4 = Point(100, 100)
print()
print(f'{p1 == p2=}')
print(f'{p3 < p1=}')
print(f'{p4 > p1=}')

try:
    print(f'{p1 <= p4=}')
except TypeError as e:
    print(f'{e=}')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

print('\n=== Implementing lte with a decorator with lt and eq already defined! ====\n')

"""
- a <= b iff a < b or a == b
- a > b iff not(a<b) and a != b
- a >= b iff not(a<b)
"""

def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and self != other
        cls.__ge__ = lambda self, other: not(self < other)
    return cls

@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 100)
print(f'{p1 == p2=}')
print(f'{p3 < p1=}')
print(f'{p4 > p1=}')
print(f'{p1 <= p4=}')
print(f'{p1 >= p4=}')
print(f'{p1 > p2=}')

print('\n=== Implementing total ordering with method from functools built-in, note we use gt instead of lt here and it still works ====\n')

from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Point):
            return abs(self) > abs(other)
        else:
            return NotImplemented

p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)
print(f'{p1 == p2=}')
print(f'{p3 < p1=}')
print(f'{p4 > p1=}')
print(f'{p1 <= p4=}')
print(f'{p1 >= p4=}')
print(f'{p1 > p2=}')
