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

"""
Multiple decorators simple example
"""

def dec_1(fn):
    def inner(*args, **kwargs):
        print('Running dec_1')
        return fn(*args,**kwargs)
    return inner

def dec_2(fn):
    def inner(*args, **kwargs):
        print('Running dec_2')
        return fn(*args,**kwargs)
    return inner

@dec_1
@dec_2
def my_func():
    print('Running my_func')

my_func()

print()

def dec_1(fn):
    def inner(*args, **kwargs):
        result = fn(*args,**kwargs)
        print('Running dec_1')
        return result
    return inner

def dec_2(fn):
    def inner(*args, **kwargs):
        result = fn(*args,**kwargs)
        print('Running dec_2')
        return result
    return inner

@dec_1
@dec_2
def my_func():
    print('Running my_func')

my_func()

print()

@dec_1
@dec_2
@logged
@timed
def my_func():
    print('Running my_func')

my_func()

"""
The order of decorators can be significant

For example, suppose you are logging calls to an API that
uses authorization:

@auth
@logged
def save_resource():
    ...

This might only log if authorization succeeds and not otherwise.

If you want to log in every case (successful auth or not), then you
might need to have it be:

@logged
@auth
def save_resource():
    ...

... instead. e.g.

save_resource = logged(auth(save_resourece))
"""
