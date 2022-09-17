# round(x, n=0)

# This will round the number x to the closest multiple of 10^-n

# You might think of this as rounding to a certain number of
# digits after the decimal point which would work for positive
# n, but n can, in fact, also be negative!

print(f'{round(123456789, -3)=}')
print(f'{type(round(123456789, -3))=}')
print(f'{round(1234.56789, 3)=}')
print(f'{type(round(1234.56789, 3))=}')
print(f'{round(123.456789, 0)=}')
print(f'{type(round(123.456789, 0))=}')
print(f'{round(123.456789)=}')
print(f'{type(round(123.456789))=}')

x = round(123.456789)
print(x)

print(f'{round(.5)=}')
print(f'{round(1 - .5)=}')
print(f'{round(.1+.1+.1+.1+.1)=}')
print(f'{round(1 - .1 - .1 - .1 - .1 - .1)=}')
print(f'{round(15,-1)}')

Note = """
Python uses banker's rounding. It rounds to the nearest value with
an even least-significant digit!
"""
print(Note)

print(f'{round(.5)=}')
print(f'{round(1.5)=}')
print(f'{round(2.5)=}')
print(f'{round(3.5)=}')

print(f'{round(5, -1)=}')
print(f'{round(15, -1)=}')
print(f'{round(25, -1)=}')
print(f'{round(35, -1)=}')

print('if you really insist on rounding away from zero, how to do it')

import math
def round_toward_infinity(x):
    return int(math.copysign(1,x)) * int(math.fabs(x) + 0.5)

print(f'{round_toward_infinity(0.5)=}')
print(f'{round_toward_infinity(1.5)=}')
print(f'{round_toward_infinity(2.5)=}')
print(f'{round_toward_infinity(3.5)=}')
print(f'{round_toward_infinity(-0.5)=}')
print(f'{round_toward_infinity(-1.5)=}')
print(f'{round_toward_infinity(-2.5)=}')
print(f'{round_toward_infinity(-3.5)=}')