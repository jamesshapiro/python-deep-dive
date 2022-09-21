"""
Some drawbacks to using Decimal class vs. floats
- not as easy to code. Construction via strings or tuples
- not all math functions that exist in the math module have a Decimal counterpart (e.g. trig functions)
- more memory overhead
- performance: much slower than floats (relatively)
"""

from decimal import Decimal
import sys

a = 3.1415
b = Decimal('3.1415')

print('larger memory footprint')
print(f'{sys.getsizeof(a)=}')
print(f'{sys.getsizeof(b)=}')

import time

def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')

n = 10_000_000
print('\nlarger time overhead')
print('\ncreation:')
start = time.perf_counter()
run_float(n)
end = time.perf_counter()

print(f'float: {end-start}')
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print(f'decimal: {end-start}')

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a

print('\naddition:')
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('larger time overhead')
print(f'float: {end-start}')
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print(f'decimal: {end-start}')



n = 5_000_000
import math

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()

print('\nsqrt:')
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('larger time overhead')
print(f'float: {end-start}')
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print(f'decimal: {end-start}')