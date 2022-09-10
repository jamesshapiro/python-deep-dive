import sys

value = 12345678

print('Simple int reference counting example:')
print(f'{sys.getrefcount(value)=}')

a = value
print(f'a = {value}')

print(f'{sys.getrefcount(value)=}')

b = a
print('b = a')
print(f'{sys.getrefcount(value)=}')

a = 11
print('a = 11')
print(f'{sys.getrefcount(value)=}')

b = a
print('b = a')
print(f'{sys.getrefcount(value)=}')