"""
Decorator Parameters

In the previous videos we saw some built-in decorators that can handle some arguments:

@wraps(fn):
def inner():
    ...

@lru_cache(maxsize=256) # <-- (function call)
def factorial(n):
    ...

This should look quite different from the decorating we have been creating and using:

@timed  # <-- (no function call)
def fibonacci(n):
    ...
"""

"""
The *timed* decorator, fixed for 10 iterations
"""
def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result
    
    return inner

"""
Can decorate with EITHER

(1.)
@timed
def my_func():
    ...

OR

(2.)
my_func = timed(my_func)

BUT this assumes we want a hard-coded value of 10, which is never a good idea
"""

# ============================================ #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
# ============================================ #


"""
First approach
"""
def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / reps
        print(avg_elapsed)
        return result
    return inner

"""
Can decorate with ONLY

my_func = timed(my_func, 10)

BUT NOT @ !!!
"""

# ============================================ #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
# ============================================ #

"""
Rethinking the solution

@timed
def my_func():
    ...

...is the same as...
my_func = timed(my_func)

So, timed is a function that returns that inner closure that contains
our original function

In order for this to work as intended:
@timed(10)
def my_func():
    ...

timed(10) will need to return our oriignal timed decorator when called

dec = timed(10) <-- timed(10) returns a decorator

@dec <-- and we decorate our function with dec
def my_func():
    ...

Nested closure work well here!
"""
def outer(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
            return result
        
        return inner
    
    return timed # <-- calling outer(n) returns our original decorator with reps set to n (free variable)

def my_func():
    pass

my_func = outer(10)(my_func)

# OR !!!

@outer(10)
def my_func():
    pass

"""
Decorator Factories

The outer function is NOT ITSELF a decorator!

Rather, it returns a decorator when called. And any arguments passed to outer
can be referenced (as free variables) inside our decorator

We call this *outer* function a decorator *factory* function. It is a function
that creates a new decorator each time it is called
"""

"""
And finally...

To wrap things up, we probably don't want our decorator call to look like:

@outer(10)
def my_func():
    ...

It would make more sense to write it this way:
@timed(10)
def my_func():
    ...

But keep in mind that timed is not the decorator itself, rather it is a
decorator factory that creates the decorator that then gets applied to my_func

Now all we need to do is change the names of the *outer* and *timed* functions
"""

def timed(reps):
    def dec(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
            return result
        
        return inner
    return dec

"""
Now we can use:

@timed(10)
def my_func():
    ...

As desired...
"""

########## CODING SECTION #########

def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f'Run time: {elapsed:.6f}s')
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

@timed
def fib(n):
    return calc_fib_recurse(n)

print(f'{fib(26)=}')

"""
Timing with multiple runs
"""

def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start
        avg_run_time = total_elapsed / 10
        print(f'Avg run time: {avg_run_time:.6f}s')
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

@timed
def fib(n):
    return calc_fib_recurse(n)

print(f'{fib(26)=}')
#print(f'{=}')
#print(f'{=}')

# ============================================ #

def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for _ in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start
        avg_run_time = total_elapsed / reps
        print(f'Avg run time: {avg_run_time:.6f}s ({reps} reps)')
        return result
    return inner

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)

print()
print(f'{fib(28)=}')

""" this works but the following does not:

@timed(5)
def fib(n):
    return calc_fib_recurse(n)

So by doing it this way, we have lost the ability
to use the @ syntax to decorate our function
"""

def dec(fn):
    print("running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
    
    return inner

def my_func():
    print("running my_func")

print()
my_func()
print()
my_func = dec(my_func)
print()
my_func()

def dec_factory():
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)
        
        return inner
    return dec

dec = dec_factory()

print('\n======= dec factory =======\n')
def my_func():
    print("running my_func")
print('> my_func = dec(my_func)')
my_func = dec(my_func)

print('\n> my_func()')
my_func()

print('These three are equivalent:')


method_1 = """
@dec
def my_func():
    print("running my_func")
"""
print(f'\nmethod 1: {method_1}')

method_2 = """
@dec_factory()
def my_func():
    print("running my_func")
"""
print(f'method 2: {method_2}')

method_3 = """
my_func = dec_factory()(my_func)
"""
print(f'method 3: {method_3}')

@dec
def my_func():
    print("running my_func")
print('method 1:')
my_func()

print('\nmethod 2:')
@dec_factory()
def my_func():
    print("running my_func")
my_func()

print('\nmethod 3:')
def my_func():
    print("running my_func")
my_func = dec_factory()(my_func)
my_func()

print('\n=== Decorator factory with arguments ===')

dec_factory_with_args = """
def dec_factory(a, b):
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            print(f"{a=}, {b=}")
            return fn(*args, **kwargs)

        return inner
    return dec
"""
def dec_factory(a, b):
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            print(f"{a=}, {b=}")
            return fn(*args, **kwargs)

        return inner
    return dec

print(dec_factory_with_args)

print('=== These three methods are equivalent... ===\n')

method_1 = """
dec = dec_factory(10, 20)

print()
# runs dec here
@dec
def my_func():
    print("running my_func")

print()
my_func()
"""
print(f'method 1: {method_1}')

method_2 = """
@dec_factory(100, 200)
def my_func():
    print("running my_func")
"""
print(f'method 2: {method_1}')

method_3 = """
def my_func():
    print("running my_func")
my_func = dec_factory(150, 250)(my_func)
"""

print(f'method 3: {method_3}')

print('\nmethod 1:')
dec = dec_factory(10, 20)
# runs dec here
@dec
def my_func():
    print("running my_func")

print()
my_func()

print('\nmethod 2:')
@dec_factory(100, 200)
def my_func():
    print("running my_func")
my_func()

print('\nmethod 3:')
def my_func():
    print("running my_func")
my_func = dec_factory(150, 250)(my_func)
my_func()

print(f'\n{"="*20}')
conclusion = """
Bottom line: we can use decorator factories to create parameterized decorators

e.g.:

@dec_factory(param_1, param_2):
def my_func():
    pass
"""
print(conclusion)

print(f'{"="*20}\n')



dec_factory_defn = """
def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_run_time = total_elapsed / reps
            print(f'Avg run time: {avg_run_time:.6f}s ({reps} reps)')
            return result
        return inner
    return timed

@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)
fib(28)
"""

print(dec_factory_defn)

def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_run_time = total_elapsed / reps
            print(f'Avg run time: {avg_run_time:.6f}s ({reps} reps)')
            return result
        return inner
    return timed

@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)
print(f'{fib(28)=}')
@dec_factory(15)
def fib(n):
    return calc_fib_recurse(n)
print(f'{fib(28)=}')







print(f'\n{"="*20}\n')
print('final piece, rename dec_factory to timed\n')
print(f'{"="*20}\n')

timed_defn = """
def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_run_time = total_elapsed / reps
            print(f'Avg run time: {avg_run_time:.6f}s ({reps} reps)')
            return result
        return inner
    return dec

@timed(5)
def fib(n):
    return calc_fib_recurse(n)
fib(28)
"""

print(timed_defn)

def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_run_time = total_elapsed / reps
            print(f'Avg run time: {avg_run_time:.6f}s ({reps} reps)')
            return result
        return inner
    return dec

@timed(5)
def fib(n):
    return calc_fib_recurse(n)
print(f'{fib(28)=}')

@timed(15)
def fib(n):
    return calc_fib_recurse(n)
print(f'{fib(28)=}')
