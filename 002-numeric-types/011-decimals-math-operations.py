# The // and % operators still satisfy the usual equation:
# n = d * (n // d) + (n % d)
# But for integers, the // operator performs floor division
# -> a // b = floor(a/b)
# For Decimals, it performs truncated division:
# -> a // b = trunc(a/b)
import decimal
from decimal import Decimal

print(f'{10 // 3=}')
print(f'{10 % 3=}')
print(f'{Decimal(10) // Decimal(3)=}')
print(f'{Decimal(10) % Decimal(3)=}')

print(f'\n{-10 // 3=}')
print(f'{-10 % 3=}')
print(f'{Decimal(-10) // Decimal(3)=}')
print(f'{Decimal(-10) % Decimal(3)=}')

print(f'\n{10 // -3=}')
print(f'{10 % -3=}')
print(f'{Decimal(10) // Decimal(-3)=}')
print(f'{Decimal(10) % Decimal(-3)=}')

print(f'\n{-10 // -3=}')
print(f'{-10 % -3=}')
print(f'{Decimal(-10) // Decimal(-3)=}')
print(f'{Decimal(-10) % Decimal(-3)=}')

print(f'\n{divmod(-10, 3)=}')
print(f'{divmod(Decimal(-10), Decimal(3))=}')

x = 10

# Some other math functions:
a = Decimal('1.5')
print(f'\n{a.ln()=}')
print(f'{a.exp()=}')
print(f'{a.sqrt()=}')

import math
print(f'{math.sqrt(a)=}')

# Note: the decimal class defines a number of operations like sqrt, logs, etc.
# BUT not all functions defined in the math module are define in the Decimal class
# for example, trig functions
# We can still use the math module
# but Decimal objects will first be cast to floats

# Hence, we lose the whole precision mechanism that motivated us to use Decimal objects
# in the first place

print()
decimal.getcontext().prec = 28
x = 0.01 # float
x_dec = Decimal('0.01')

import math
root = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print(f'{x=}')
print(f'{x_dec=}')
print(f'{root=:.28f}')
print(f'{root_mixed=:.28f}')
print(f'{root_dec=:.28f}')
print(f'{root*root=:.28f}')
print(f'{root_mixed*root_mixed=:.28f}')
print(f'{root_dec*root_dec=:.28f}')