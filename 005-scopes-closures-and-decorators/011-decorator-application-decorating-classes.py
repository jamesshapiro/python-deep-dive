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

Fraction.speak = 100

print(f'{f.speak=}')

Fraction.speak = lambda self: f'I am {self}'