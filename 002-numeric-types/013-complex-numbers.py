# The complex class

# Constructor complex(x, y)
# x -> real part
# y -> imaginary part
# Literals: x + yJ

# Example:
a = complex(1,2)
b = 1 + 2j
print(f'{a == b=}') #-> True

print(f'{a.real=}')
print(f'{a.imag=}')
print(f'{a.conjugate()=}')

# other operations
print(f'{complex(1,2) + complex(3,4)}')
print(f'{complex(1,2) - complex(3,4)}')
print(f'{complex(1,2) / complex(3,4)}')
print(f'{complex(1,2) * complex(3,4)}')
print(f'{complex(1,2) ** 3}')

# // and % are not supported

# == and != are supported but raise the same issues as floats because
# complex numbers are essentially made up of two floats

# comparison operators such as <, >, <= and >= are not supported

# functions in the math module will not work

# Use the cmath module instead
# - exponentials
# - logs
# - trig and inverse trig functions
# - hyperbolics and inverse hyperbolics
# - polar / rectangular conversions
# - isclose method (as with math module)

print('\nrectangular to polar:')
import cmath
# this returns phi, where phi \in [-pi, pi] measured counterclockwise from
# the real axis, essentially the angle in radians
print(f'{cmath.phase(a)=}')

# this returns the magnitude (r) of x
print(f'{abs(a)=}')

a = -1 + 0j

print(f'{a=}')
print(f'{cmath.phase(a)=}')
print(f'{abs(a)=}')

a = -1j

print(f'{a=}')
print(f'{cmath.phase(a)=}')
print(f'{abs(a)=}')

a = 1 + 1j

import math
print(f'{a=}')
print(f'{math.pi / 4=}')
print(f'{cmath.phase(a)=}')
print(f'{abs(a)=}')

print('\npolar to rectangular:')
print(f'{cmath.rect(math.sqrt(2), math.pi/4)}')

print('e^(i*pi) + 1 = 0')
print(f'{cmath.exp(cmath.pi*1j)+1=}')
print(f'{cmath.isclose(cmath.exp(cmath.pi*1j)+1, 0, abs_tol=0.0001)=}')

a = complex(1,2)
b = 1 + 2j
print(f'{a==b=}')
print(f'{a.real=}')
print(f'{type(a.real)=}')

a = 0.1j
print(f'{a.imag=:.25f}')
print(f'{a+a+a==0.3j=}')

import math
math.sqrt(2)
math.pi
import cmath

print(f'{cmath.pi=}')
print(f'{type(cmath.pi)=}')

a = 1 + 1j
print('\nRectangular to polar')
print('a = 1 + 1j')
print(f'{cmath.phase(a)=}')
print(f'{math.pi/4=}')
print(f'{abs(a)=}')

print('\nPolar to rectangular')
print(f'{cmath.rect(math.sqrt(2), math.pi/4)=}')

print('\ne^(i*pi)+1=0')
print(f'{cmath.exp(cmath.pi*1j)+1=}')
print(f'{cmath.exp(complex(0, math.pi))+1=}')
rhs = cmath.exp(complex(0, math.pi))+1
print(f'{cmath.isclose(rhs, 0, abs_tol=0.0001)=}')