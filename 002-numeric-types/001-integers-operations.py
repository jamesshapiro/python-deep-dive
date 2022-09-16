"""
The int data type
Ex: 0, 10, -100, 10_000_000

How large can a Python int become (positive or negative)?

The int object uses a *variable* number of bits

Can use 4 bytes (32 bits), 8 bytes, 12 bytes, etc.

And it's completely seamless to us
"""

print(type(100))

import sys

print('24 bytes of overhead')
print(f'{sys.getsizeof(0)=}')
print(f'{sys.getsizeof(1)=}')
print(f'{sys.getsizeof(2**1000)=}')

print('larger ints result in slower calculations')

import time

def calc(a):
    start = time.perf_counter()
    for i in range(10_000_000):
        l.a * 2
    end = time.perf_counter()
    print(end - start)

calc(10)
calc(2**100)
calc(2**10_000)    