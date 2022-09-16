"""
most integer operations with two operands return an int:

+ is (int, int) -> int
- is (int, int) -> int
* is (int, int) -> int
** is (int, int) -> int
// is (int, int) -> int
% is (int, int) -> int

but

/ is (int, int) -> float
"""

print('floor division with negative numerator')
print('the floor of a real number x is the largest integer <= x')
print(f'{-7//5=}')
print('-7/5 == -1.4')
print('floor(-1.4) == -2')

print('\nmodulus with negative numerator')
print(f'{-7 % 5=} !!!')
print('------------')
print(f'{-7 // 5=}')
print('a = b * (a // b) + a % b')
print('a % b  =  a - b * (a // b)')
print('-7 % 5 = -7 - 5 * (-7 // 5)')
print('       = -7 - 5 * (-2) ')
print('       = -7 + 10 ')
print('       =  3 ')

print('\nfloor division with negative denominator')
print('the floor of a real number x is the largest integer <= x')
print(f'{7//-5=}')
print('7/-5 == -1.4')
print('floor(-1.4) == -2')

print('\nmodulus with negative numerator')
print(f'{7 % -5=} !!!')
print('Note: this is the negation of -7 % 5 !!!')
print('------------')
print(f'{7 // -5=}')
print('a = b * (a // b) + a % b')
print('a % b  =  a - b * (a // b)')
print('7 % -5 = 7 - -5 * (7 // -5)')
print('       = 7 +  5 * (-2)')
print('       = 7 - 10')
print('       = -3')

print('\nfloor division with two negatives')
print('the floor of a real number x is the largest integer <= x')
print(f'{-7//-5=}')
print('-7/-5 == 1.4')
print('floor(1.4) == 1')

print('\nmodulus with two negatives')
print(f'{-7 % -5=} !!!')
print('------------')
print(f'{-7 // -5=}')
print('a = b * (a // b) + a % b')
print('a % b   =  a - b * (a // b)')
print('-7 % -5 = -7 - -5 * (-7 // -5)')
print('-7 % -5 = -7 +  5 * (1)')
print('-7 % -5 = -7 +  5')
print('-7 % -5 = -2')

print(f'{type(1+1)=}')
print(f'{type(1-1)=}')
print(f'{type(1*1)=}')
print(f'{type(1%1)=}')
print(f'{type(1//1)=}')
print(f'{type(1/1)=}')

import math
print(f'{math.floor(3.15)=}')
print(f'{math.floor(3.999999)=}')
print(f'{math.floor(-3.14)=}')
print(f'{math.floor(-3.0000001)=}')
print('\nThis happens because of the limited precision of floats:')
print(f'{math.floor(-3.00000000000000000000001)=}')
