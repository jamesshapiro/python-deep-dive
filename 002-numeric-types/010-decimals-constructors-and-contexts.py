"""
Constructing Decimal Objects
import decimal
from decimal import Decimal
Decimal(x) # x can be:
- an integer
- other Decimals
- strings
- floats (but not recommended because the entire point of the module is to avoid float imprecision)
"""

import decimal
from decimal import Decimal
print(f'{Decimal(10)=}')
print(f'{Decimal("0.1")=}')
print(f'{Decimal((1, (3,1,4,1,5), -4))=}')
print('float constructor anti-pattern:')
print(f'{Decimal(0.1)=}')

# Using the tuple constructor:
# 1.23 -> +123 X 10^-2
print(f'{Decimal((0, (1,2,3), -2))=}')
print(f'{Decimal((0, (0,0,0), -2))=}')

# Context precision and the constructor
# Context precision affects mathematical operations
# Context precision does NOT affect the constructor

decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
print(f'{a=}')
print(f'{b=}')
print(f'{a+b=}')

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(f'{c=}')

print(f'{c=}')
