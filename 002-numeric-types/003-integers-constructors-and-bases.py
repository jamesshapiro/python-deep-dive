import decimal

a = int(10)
print(a)
a = int(-10)
print(a)
a = int(10.9)
print(a)
a = int(-10.9)
print(a)

print('Note: int constructor truncates')

a = int(True)
print(a)

a = int(decimal.Decimal("10.9"))
print(a)

print('\nNumber Base examples: ')
base_10_default = int("123")
print(base_10_default)

binary = int("1010", 2)
print(binary)

base_16 = int("A12F", base=16)
print(f'{base_16=}')

print('You can use up to base 36, because that is the digits plus the alphabet')

print('\n')

try:
    int("2",2)
except ValueError:
    print("ValueError! int('2',2) throws an error because binary digits can only be 0 or 1")

print('\nYou can also go from decimal to some other bases')
print(f'{bin(10)=}')
print(f'{oct(10)=}')
print(f'{hex(10)=}')

print(f'{int("0xA",16)=}')
print('However, there is no built-in support for arbitrary bases')

print('\nBase Change Algorithm')

def base_change(n, b):
    encodings = '0123456789abcdefghijklmnopqrstuvwxyz'
    digits = []
    while n > 0:
        m = n % b
        n = n // b
        digits.insert(0,encodings[m])
    return ''.join(digits)

print(f'{base_change(1485,16)=}')
print(f'{base_change(1485,2)=}')
print(f'{base_change(1485,36)=}')

import fractions
a = fractions.Fraction(1,7)
print(f'{a=}')
print(f'{float(a)=}')
print(f'{int(a)=}')

print('b = 0b101')
b = 0b101
print(f'{b=}')

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

print(f'{from_base10(10, 2)=}')

def encode(digits):
    digit_map = '0123456789abcdefghijklmnopqrstuvwxyz'
    if max(digits) > len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    return ''.join(digit_map[d] for d in digits)

print(f'{encode([15, 15])=}')

def rebase_from10(number, base):
    digit_map = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_base10(number, base)
    encoding = encode(digits)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

print('e = rebase_from10(100,2)')
e = rebase_from10(100,2)
print(f'{e=}')
print(f'{int(e, base=2)=}')