print('Again, try running these examples interactively:\n')

# Constant expressions:
# e.g. numeric calculations
a = 24 * 60 # Python will actually pre-calculate 24 * 60 -> 1440

# short sequences (length < 20):
(1,2)*5
'abc' * 3
'hello' + ' world'

# but NOT
'the quick brown fox' * 10

# Membership tests: Mutables are replaced by immutables
# When membership tests such as:

# if e in [1,2, 3]

# are encountered, the [1,2,3] constant is replaced by its
# immutable counterpart, the (1,2,3) tuple

# lists -> tuples
# sets -> frozensets

# Set membership is much faster than list or tuple membership
# because sets are basically like dictionaries, backed by a hashmap

def my_func():
    a = 24 * 60
    b = (1,2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3

print(my_func.__code__.co_consts)

def my_func(e):
    if e in [1,2,3]:
        pass

print(my_func.__code__.co_consts)

def my_func(e):
    if e in {1,2,3}:
        pass

print(my_func.__code__.co_consts)

import string
import time

print(string.ascii_letters)
char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

for container in [char_list, char_tuple, char_set]:
    start = time.perf_counter()
    membership_test(10_000_000, container)
    end = time.perf_counter()
    print(f'Time: {end - start} with {container}')
    