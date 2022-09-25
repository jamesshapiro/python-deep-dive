"""
The use case for *

We don't always want to unpack every single item in an iterable

We may, for example, want to unpack the first value, and then unpack
the remaining values into another variable

l = [1,2,3,4,5,6]

We can achieve this with slicing:
    a = l[0]
    b = l[1:]

Simple unpacking alternative (aka parallel assignment):
a, b = l[0], l[1:]

We can also use the * operator:
a, *b = l

Apart from cleaner syntax, it also works with any iterable, not just
sequence types. For example, it works with sets even though they
don't support slicing
"""

a, *b = [-10,5,2,100]
print(f'{a=}, {b=}')

print('\nNote that b always gets unpacked into a list, regardless of what the source is (list, string, tuple, dict, etc.)')
a, *b = (-10,5,2,100)
print(f'{a=}, {b=}')

a, *b = 'XYZ'
print(f'{a=}, {b=}')

a,b,*c = 1,2,3,4,5
print(f'{a=}, {b=}, {c=}')

a,b,*c,d = 1,2,3,4,5
print(f'{a=}, {b=}, {c=}, {d=}')

"""
The * operator can only be used once in the LHS of an unpacking argument (need to be able to count a 
fixed number of arguments before and after it (or just before, or just after)
"""

print('\nWe can also use unpacking as follows:')
l1 = [1,2,3]
l2 = [4,5,6]
l = [*l1, *l2]
print(f'{l=}')

l1 = [1,2,3]
l2 = 'XYZ'
l = [*l1, *l2]
print(f'\n{l=}')

print('\nWhat about sets/dicts?')
"""
Sets have no order, so this type of positional unpacking doesn't make very much sense.
But here is a case where it might:
"""

d_1 = {'p':1, 'y':2}
d_2 = {'t':3, 'h':4}
d_3 = {'h':5, 'o':6, 'n': 7} # Note that "h" is repeated in d_2 and d_3

l = [*d_1, *d_2, *d_3]
s = {*d_1, *d_2, *d_3}

print(f'{l=}')
print(f'{s=}')

"""
The ** unpacking operator

When working with dictionaries we saw that * essentially iterated the keys

** is how we unpack the key-value pairs of the dictionary

Note that ** cannot be used in the left-hand-side of an assignment
"""

d = {**d_1, **d_2, **d_3}
print(f'{d=}')
print('Note that the value of "h" in d_3 "overwrote" the first value of "h" found in d_2')
print('The order matters (later args will overwrite earlier ones')

d_1 = {'a':1, 'b':2}
new_dict = {'a': 10, 'c': 3, **d_1}
print(f'{new_dict=}')
new_dict = {**d_1, 'a': 10, 'c': 3}
print(f'{new_dict=}')

"""
Nest Unpacking

Python will support nested unpacking as well
l = [1,2,[3,4]]
"""
l = [1,2,[3,4]]
a,b,c = l
d,e = c
print(f'{a=}, {b=}, {d=}, {e=}')

a,b,(d,e) = l
print(f'{a=}, {b=}, {d=}, {e=}')

a, *b, (c,d,e) = [1,2,3,'XYZ']
print(f'{a=}, {b=}, {c=}, {d=}, {e=}')

print('\nIt is okay to use multiple *s on the LHS if they are nested')
a, *b, (c, *d) = [1,2,3, 'python']
print(f'{a=}, {b=}, {c=}, {d=}')

print('\nConcise set to list')
s = {'d', 10, 3, -99}
*c, = s
print(f'{c=}')

print('\nMerging sets')
s_1 = {10, 3, -99}
s_2 = {10, 20, 30}
combined = {*s_1, *s_2}
print(f'{combined=}')

print('\nMerging 3+ sets')
s_1 = {1, 2, 3}
s_2 = {3, 4, 5}
s_3 = {5, 6, 7}
s_4 = {7, 8, 9}
combined = {*s_1, *s_2, *s_3, *s_4}
print(f'{combined=}')

print('\nMerging dicts')
d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 4}
combined = {*d1, *d2}
print(f'{combined=}')

combined = {**d1, **d2}
print(f'{combined=}')
combined = {**d2, **d1}
print(f'{combined=}')