# Side note on Tuples:
# What defines a tuple in Python is not "()", but ","

# 1,2,3 is also a tuple -> (1,2,3)
# The "()" are used to make the tuple clearer

x = 1,2,3
print(f'{x=}')
print(f'{type(x)=}')

print('to create a tuple with a single element')

# Don't do this: x = (1)
print('\nx = (1)')
x = (1)
print(f'{x=}')
print(f'{type(x)=}')
# Do this:

print('\nx = (1,)')
x = (1,)
print(f'{x=}')
print(f'{type(x)=}')

print('\nx = 1,')
x = 1,
print(f'{x=}')
print(f'{type(x)=}')

print('\nTo create an empty tuple')
print('\nx = ()')
x = ()
print(f'{x=}')
print(f'{type(x)=}')
print('\nx = tuple()')
x = tuple()
print(f'{x=}')
print(f'{type(x)=}')

"""
Packed Values
"Packed Values" refers to values that are bundled together in some way

Tuples and Lists are obvious. Strings are also considered to be packed values
as are sets and dictionaries

In fact, any iterable can be considered a packed value

Unpacking Packed Values
"Unpacking" is the act of splitting packed values into individual variables
contained in a list or tuple
"""

a, b, c = [1,2,3]
print(f'{a=},{b=},{c=}')

"""
3 elements in [1,2,3] -> we need 3 variables to unpack

"a,b,c" is actually a tuple of 3 variables: a,b, and c

a -> 1, b -> 2, c -> 3

The unpacking into individual variables is based on the relative positions
of each element, exactly the same as with how positional arguments are
assigned to parameters in a function

Unpacking other iterables, e.g. a tuple:
"""

a, b, c = 10, 20, 'hello'
print(f'{a=},{b=},{c=}')
a, b, c = 'XYZ'
print(f'{a=},{b=},{c=}')

a, b = 10, 20
print(f'{a=},{b=}')

"""
In fact, unpacking works with any iterable type

for e in 10, 20, 'hello' -> loop returns 10, 20, 'hello'
for e in 'XYZ'           -> loop returns 'X', 'Y', and 'Z'
"""
print('\nSwapping two variables example')
a = 'a'
b = 'b'
a, b = b, a
print(f'{a=},{b=}')

d = {'key_1': 1, 'key_2': 2, 'key_3': 3}
a,b,c = d

print('Dictionary example')
print('Note that this is an unordered type so the keys can appear in any order')
print(f'{a=},{b=},{c=}')

s = {'p', 'y', 't', 'h', 'o', 'n'}
a,b,c,d,e,f = s
print(f'{a=},{b=},{c=},{d=},{e=},{f=}')

(a,b,c) = [1,2,3]
print(f'{a=},{b=},{c=}')

a,b,c = 10, {1,2}, ['a','b']
print(f'{a=},{b=},{c=}')

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a,b,c,d = my_dict.values()
print(f'{a=},{b=},{c=},{d=}')
a,b,c,d = my_dict.items()
print(f'{a=},{b=},{c=},{d=}')

print('\nloop example')
for a,b in my_dict.items():
    print(f'key={a}, value={b}')