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