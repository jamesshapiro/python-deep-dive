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

# However absolute tolerance doesn't work well in practice, because
# for large numbers you would want a higher tolerance and for tiny
# numbers you might want a smaller one

# You can do something like a relative tolerance of 0.1%, so:
# tol = rel_tol * max(|x|,|y|), but note that this does not
# work well for numbers close to zero

# We can combine *both* methods, calculating absolute and relative
# tolerances and using the larger of the two tolerances
# tol = max(rel_tol * max(|x|, |y|), abs_tol)

# PEP 485

# the math module has that built in for us!

# math.isclose(a,b,*, rel_tol=1e-09, abs_tol=0.0)

# But WARNING, if you do not specify abs_tol, then it defaults
# to zero and you will face the problem we encountered when
# comparing numbers close to zero!

x = 1000.0000001
y = 1000.0000002

print(f'{x=}')
print(f'{y=}')
print(f'{math.isclose(x,y)=}')

a = 0.0000001
b = 0.0000002

print(f'{a=}')
print(f'{b=}')
print(f'{math.isclose(a,b)=}')
print(f'{math.isclose(x,y, abs_tol=1e-5)=}')
print(f'{math.isclose(a,b, abs_tol=1e-5)=}')

x = 1000.01
y = 1000.02
print(f'{x=}')
print(f'{y=}')
print(f'{math.isclose(x,y, rel_tol=1e-5, abs_tol=1e-5)=}')

a = 0.01
b = 0.02
print(f'{a=}')
print(f'{b=}')
print('As desired: ')
print(f'{math.isclose(a,b, rel_tol=1e-5, abs_tol=1e-5)=}')