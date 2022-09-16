from fractions import Fraction

x = Fraction(3,4)
y = Fraction(22,7)
z = Fraction(6,10)

# Fractions are automatically reduced

print(f'{z=}')

# Negative signs are always attached to the numerator

k = Fraction(1,-4)
print(f'{k=}')

# Constructors
# Fraction(num, denom)
# Fraction(other_fraction)
# Fraction(float)
# Fraction(decimal)

import math
print(math.pi)
print(f'{Fraction(math.pi)=}')

print(f"{Fraction('10')=}")
print(f"{Fraction('22/7')=}")
print(f"{Fraction(2,3)*Fraction(1,2)=}")

x = Fraction(22,7)
print(x.numerator)
print(x.denominator)

print('WARNING: ')
print(f'{Fraction(0.3)=}')

print(format(0.3, '.5f'))
print(format(0.3, '.25f'))

# Given a Fraction object, we can find an approximate equivalent fraction
# with a constrained denominator using the limit_denominator instance method

x = Fraction(.3)
print(f'{x.limit_denominator(10)=}')

x = Fraction(math.pi)
print(f'{x.limit_denominator(10)=}')
print(f'{x.limit_denominator(100)=}')
print(f'{x.limit_denominator(1000)=}')