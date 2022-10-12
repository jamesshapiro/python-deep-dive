"""
Reducing Functions in Python

These are functions that recombine an iterable recursively, ending up with a single return value

Also called "accumulators", "aggregators", or "folding functions".

Example: Finding the maximum value in an iterable

sequence: a_0, a_1, a_2, ..., a_{n-1}
max(a, b) -> maximum of a and b

result = a_0
result = max(result, a_1)
result = max(result, a_2)
...
result = max(result, a_{n-1})

Because we have not studied iterables in general, we will stay with the special case of sequences
(i.e. we can use indexes to access elements in the sequence)

Using a loop:

"""
l = [5,8,6,10,9]
max_value = lambda a,b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = max_value(result, e)
    return result

min_value = lambda a,b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = min_value(result, e)
    return result

# Generalizing...:

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

_reduce(lambda a,b: a if a > b else b, l) # -> maximum
_reduce(lambda a,b: a if a < b else b, l) # -> min
print(f'{_reduce(lambda a,b: a+b, l)=}') # -> sum

"""
The functools module

Supports all iterables, not just sequences
"""

from functools import reduce

l = [5,8,6,10,9]
print(f'{reduce(lambda a,b: a if a > b else b, l)=}')
print(f'{reduce(lambda a,b: a if a < b else b, l)=}')
print(f'{reduce(lambda a,b: a+b, l)=}')
print('functools reduce works on any iterable. E.g.:')
print(f'{reduce(lambda a,b: a if a > b else b, {10,5,2,4})=}')
print(f'{reduce(lambda a,b: a if a < b else b, "python")=}')
print(f'{min("python")=}')
print(f'{reduce(lambda a,b: a + " " + b, "python")=}')
print(f'{reduce(lambda a,b: a + " " + b, ("python", "is", "great"))=}')

"""
Built-in Reducing Functions

Python provides several common reducing functions:
- min
- max
- sum
- any
- all
- join
"""


print('Calculating the product of all elements in an iterable:')
"""
No built-in method to do this

But very similar to the addition case
"""

"""
The reduce initializer

The reduce function has a third (optional) parameter: initializer (defaults to None)

If specified, it is like adding it to the front of the iterable.

Often used to provide some kind of default in case the iterable is empty.
"""

print(f'{reduce(lambda a,b: a*b, l)=}')
l = []
try:
    print(f'{reduce(lambda a,b: a+b, l)=}')
except TypeError as e:
    print(e)
print(f'{reduce(lambda a,b: a+b, l, 0)=}')

def fact(n):
    return reduce(lambda a, b: a*b, range(1,n+1))

print(f'{fact(6)=}')
#print(f'{=}')