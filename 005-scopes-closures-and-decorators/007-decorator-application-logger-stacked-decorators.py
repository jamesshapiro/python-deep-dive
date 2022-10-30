"""
Decorator Application (Logger, Stacked Decorators)
"""

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}')
        return result
    
    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1()
func_2()

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f'{fn.__name__} ran for {elapsed:.6f}s')
        return result
    
    return inner

@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1,n+1))

print()
print(f'{fact(3)=}')
print(f'{fact(5)=}')

@logged
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1,n+1))

print()
print(f'{fact(3)=}')
print(f'{fact(5)=}')
print()

"""
Can decorate a function with multiple decorators
"""

@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1,n+1))

print(f'{fact(3)=}')
print(f'{fact(5)=}')
print()


def dec_1(fn):
    def inner(*args, **kwargs):
        print('Running dec_1')
        return fn(*args,**kwargs)

#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
