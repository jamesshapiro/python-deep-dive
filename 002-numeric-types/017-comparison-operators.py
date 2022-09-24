"""
Categories of Comparison Operators
- binary operators
- evaluate to a bool value

Identity Operations   is, is not      # compares memory address, any type
Value Comparisons     ==, !=          # compares values, different types okay, but must be compatible
Ordering Comparisons  <, <=, >, >=    # doesn't work for all types
Membership Operations in, not in      # used with iterable types
"""

#print(f'{=}')

print(f'{type("")==str=}')

from decimal import Decimal
from fractions import Fraction
import math

print(f'{10.0==Decimal("10.0")=}')
print(f'{0.1==Decimal("0.1")=}')
print(f'{Decimal("0.125")==Fraction(1,8)=}')
print(f'{True==1=}')
print(f'{True==Fraction(3,3)=}')

print(f'{1< 3.14=}')
print(f'{Fraction(22,7)>math.pi=}')
print(f'{Decimal("0.5")<=Fraction(2,3)=}')
print(f'{True<Decimal("3.14")=}')
print(f'{Fraction(2,3)>False=}')

note = """
NOTE:
a == b == c -> a == b and b == c
a < b < c   -> a < b and b < c
a < b > c   -> a < b and b > c
"""
print(note)
print(f'{Decimal("0.125")==Fraction(1,8)==0.125=}')
print(f'{Decimal("0.125")<=Fraction(1,8)<=0.125=}')
print(f'{5<6>2=}')
print(f'{"A"<"a"<"z">"Z"in"Zebra"=}')
