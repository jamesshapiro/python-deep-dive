"""
Operator Precedence:

()
< > <= >= == != in is
not
and
or
"""

import string
print('not relevant to this lecture, just good to know')
print(f'{string.ascii_letters=}')
print(f'{string.ascii_uppercase=}')
print(f'{string.digits=}')

print('clever trick to avoid division by zero')
a = 2
b = 0
print(f'{b and a/b=}')


print('with assignment')
total = 100
a = 10

x = a and total/a

a = 0

x = a and total/a

print('clever trick to return first character or empty string')
s = 'hello'

result = (s and s[0]) or ''
print(f'{result=}')

s = ''
result = (s and s[0]) or ''
print(f'{result=}')

print('retrieving from a database')
s1 = None
s2 = ''
s3 = 'abc'

result = (s1 and s1[0]) or 'n/a'
print(f'{result=}')
result = (s2 and s2[0]) or 'n/a'
print(f'{result=}')
result = (s3 and s3[0]) or 'n/a'
print(f'{result=}')