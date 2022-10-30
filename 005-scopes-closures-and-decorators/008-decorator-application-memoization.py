"""
Decorator Application (Memoization)
"""

"""
Stupid naive method
"""
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

#fib(10)
"""
Memoization with a simple class
"""

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2:1}
    
    def fib(self, n):
        if n not in self.cache:
            print(f'Calculating fib({n}) -- class')
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()
f.fib(10)

"""
Memoization with a closure
"""

def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print(f'Calculating fib({n}) -- closure')
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    
    return calc_fib

f = fib()
print()
print(f'{f(10)=}')
print(f'{f(10)=}')

g = fib()
print()
print(f'{g(10)=}')
print(f'{g(10)=}')

"""
Memoization with a decorator
"""

def memoize_fib(fib):
    cache = {1: 1, 2: 1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    
    return inner

@memoize_fib
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print('\nMemoized example:')
print(f'{fib(10)=}')

"""
Memoization with a decorator v2
"""
def memoize(fn):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return inner

@memoize
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print('\nMemoized example:')
print(f'{fib(10)=}')
print(f'{fib(10)=}')
print(f'{fib(12)=}')

def fact(n):
    print(f'Calculating fact({n})')
    return 1 if n < 2 else n * fact(n-1)

print()
print('Non-memoized:')
print(f'{fact(6)=}')
print(f'{fact(7)=}')

@memoize
def fact(n):
    print(f'Calculating fact({n})')
    return 1 if n < 2 else n * fact(n-1)

print()
print('Memoized:')
print(f'{fact(6)=}')
print(f'{fact(7)=}')

from time import perf_counter

@memoize
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print()
print('Memoized:')
start = perf_counter()
print(f'{fib(35)=}')
end = perf_counter()
print(end-start)

"""
Limiting the size of the memoization cache
"""
from functools import lru_cache

@lru_cache()
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print()
print(f'{fib(10)=}')
print(f'{fib(11)=}')

@lru_cache(maxsize=8)
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print()
print('LRU with cache size set')
print(f'{fib(10)=}')
print(f'{fib(16)=}')
print(f'{fib(8)=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
