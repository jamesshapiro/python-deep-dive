print(float(10))
print(float(10.4))
print(float(12.5))

#print(float('22/7')) will not work

from fractions import Fraction

print(float(Fraction('22/7')))

print(0.1)

print(format(0.1, '.25f'))
print(format(0.125, '.25f'))

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
print(format(a, '.25f'))
print(format(b, '.25f'))