"""
Closures Applications (Part 1)
"""
class Averager:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()

print(f'{a.add(10)=}')
print(f'{a.add(20)=}')
print(f'{a.add(30)=}')

b = Averager()
print(f'{b.add(10)=}')

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()

print(f'{a(10)=}')
print(f'{a(20)=}')
print(f'{a(30)=}')

b = averager()
print(f'{b(10)=}')
print(f'{a.__closure__=}')
print(f'{b.__closure__=}')

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    return add

a = averager()

print(f'{a(10)=}')
print(f'{a(20)=}')
print(f'{a(30)=}')

b = averager()
print(f'{b(10)=}')
print(f'{a.__closure__=}')
print(f'{b.__closure__=}')
print(f'{a.__code__.co_freevars=}')

"""
Another application
"""
import time
from time import perf_counter
perf_counter()
perf_counter()

class Timer:
    def __init__(self):
        self.start = perf_counter()
    
    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()
print()
time.sleep(0.5)
print(f'{t1()=}')

"""
Closure version
"""
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()
time.sleep(0.5)
print(f'{t2()=}')

"""
Closures Applications (Part 2)
"""
def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter_1 = counter()
print()
print(f'{counter_1()=}')
print(f'{counter_1()=}')

"""
Count how many times a function has been run
"""
def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f'{fn.__name__} has been called {cnt} times')
        return fn(*args, **kwargs)
    return inner

def add(a,b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)
print(f'{counter_add.__closure__=}')
print(f'{counter_add(1,2)=}')
print(f'{counter_add(10,20)=}')
print(f'{counter_add(100,200)=}')
print(f'{counter_add.__code__.co_freevars=}')

counter_mult = counter(mult)
print()
print(f'{counter_mult.__closure__=}')
print(f'{counter_mult(1,2)=}')
print(f'{counter_mult(10,20)=}')
print(f'{counter_mult(100,200)=}')
print(f'{counter_mult.__code__.co_freevars=}')

"""
Globally storing the invocation count
"""
counters = {}
def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner
counted_add = counter(add)
counted_mult = counter(mult)
print()
print(f'{counted_add(1,2)=}')
print(f'{counted_add(10,20)=}')
print(f'{counted_add(100,200)=}')
print()
print(f'{counted_mult(1,2)=}')

print(f'{counters=}')

"""
Globally storing the invocation count
with a potentially non-global object
"""

#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
