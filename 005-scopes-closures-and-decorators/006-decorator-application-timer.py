"""
Decorator Application (Timing)
"""
import time

def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end-start
        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print(f'{fn.__name__}({args_str}) took {elapsed:.6f}s to run.')
        return result
    return inner

"""
Three ways to calculate Fibonacci numbers

1. recursion
2. loop
3. reduce
"""

# @timed -- don't do this because it will give too many timings
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

print(f'{calc_recursive_fib(6)=}')

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)

print(f'{fib_recursive(6)=}')
print(f'{fib_recursive(20)=}')
print(f'{fib_recursive(25)=}')
print(f'{fib_recursive(30)=}')
print(f'{fib_recursive(33)=}')

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(f'{fib_loop(6)=}')
print(f'{fib_loop(20)=}')
print(f'{fib_loop(25)=}')
print(f'{fib_loop(30)=}')
print(f'{fib_loop(33)=}')
print(f'{fib_loop(3333)=}')

"""
Reduce example:

n = 1:
(1,0) --> (1,1) 
result index[0]

n = 2:
(1,0) --> (1,1) --> (2,1)
result index[0]

n = 3:
(1,0) --> (1,1) --> (2,1) --> (3,2)
result index[0]

n = 3:
(1,0) --> (1,1) --> (2,1) --> (3,2) --> (5,3)
result index[0]

prev value = (a, b)
new value  = (a+b, a)
"""

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1,0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                   dummy,
                   initial
                  )
    return fib_n[0]

print(f'{fib_reduce(6)=}')
print(f'{fib_reduce(20)=}')
print(f'{fib_reduce(25)=}')
print(f'{fib_reduce(30)=}')
print(f'{fib_reduce(33)=}')
print(f'{fib_reduce(3333)=}')

def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        for i in range(10):
            print(f'Running iteration {i}...')
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1        
        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        elapsed_avg = elapsed_total / elapsed_count
        print(f'{fn.__name__}({args_str}) took {elapsed_avg:.6f}s to run.')
        return result
    return inner

@timed
def fib_reduce(n):
    initial = (1,0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                   dummy,
                   initial
                  )
    return fib_n[0]

print(f'{fib_reduce(100)=}')

"""
Parameterizing: Sub-optimal solution
"""
def timed(fn, count):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        for i in range(count):
            print(f'Running iteration {i}...')
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1        
        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        elapsed_avg = elapsed_total / elapsed_count
        print(f'{fn.__name__}({args_str}) took {elapsed_avg:.6f}s to run.')
        return result
    return inner

@timed
def fib_reduce(n):
    initial = (1,0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                   dummy,
                   initial
                  )
    return fib_n[0]

"""
But this is a bad method because it does not work with @
"""

fib_reduce = timed(fib_reduce, 15)
fib_reduce(100)
