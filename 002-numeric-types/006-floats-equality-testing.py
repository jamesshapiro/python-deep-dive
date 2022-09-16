a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
print(format(a, '.25f'))
print(format(b, '.25f'))

print(f'{round(a, 5) == round(b, 5)=}')

import math

def is_equal(x, y, eps):
    return math.fabs(x-y) < eps

print(f'{is_equal(a,b,.000000000001)=}')