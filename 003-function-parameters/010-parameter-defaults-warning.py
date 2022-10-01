"""
What happens at run-time...

When a module is loaded: all code is executed immediately

Module Code:
a = 10 # the integer object 10 is created and "a" references it

def func1(a):
    print(a)

# ^^ here the function object is created and "func1" references it

func1(a) # here the function is actually executed

What about default values?

Module Code:
def func1(a=10):
    print(a)

# ^^ here the function object is created and "func1" references it.
  Moreover, the integer object 10 is evaluated/created and is assigned
  as the default value for a

func1() # the function is executed

# By the time this happens, the default value for a has *already* been
evaluated and assigned -- it is *not re-evaluated* when the function is called

Consider this:
We want to create a function that will write a log entry to the console with
a user-specified event date/time. If the user does not supply a date/time, we
want to set it to the current date/time
"""

from datetime import datetime
import time

def log(msg, *, dt=datetime.utcnow()):
    print(f'{dt}: {msg}')

DELAY = 1
log('message 1')
time.sleep(DELAY)
log('message 2')
print('NOTE: time has elapsed, but dt is set when the code is initialized')

print('\nSolution Pattern')
def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f'{dt}: {msg}')

time.sleep(DELAY)
log('message 3')
time.sleep(DELAY)
log('message 4')

"""
In general, always before of using a *mutable* object (or a callable) for an argument default
"""

print('\nAnother pitfall:')
def add_item(name, quantity, unit, grocery_list):
    grocery_list.append(f'{name} ({quantity} {unit})')
    return grocery_list

store_1 = []
store_2 = []

add_item('banana', 2, 'fingers', store_1)
add_item('milk', 1, 'liter', store_1)
print(store_1)

add_item('python', 1, 'medium-rare', store_2)
print(store_2)

# motivation for pitfall:
# if the user forgets to provide a list, create one!
def add_item(name, quantity, unit, grocery_list=[]):
    grocery_list.append(f'{name} ({quantity} {unit})')
    return grocery_list

del store_1
del store_2

store_1 = add_item('banana', 2, 'fingers')
add_item('milk', 1, 'liter', store_1)
print(f'{store_1=}')

store_2 = add_item('python', 1, 'medium-rare')
print(f'{store_2=}')
print(f'{store_1=}')
print('!!!')
print('What is happening here is that the default list was created once, during function creation, and the function will always use the same list and provide that shared instance')

print('\nHow to solve? Standard pattern:')

def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append(f'{name} ({quantity} {unit})')
    return grocery_list

del store_1
del store_2

store_1 = add_item('banana', 2, 'fingers')
add_item('milk', 1, 'liter', store_1)
print(f'{store_1=}')

store_2 = add_item('python', 1, 'medium-rare')
print(f'{store_2=}')
print(f'{store_1=}')

print('\nExample where we might want to actually leverage shared state')

def factorial(n):
    if n < 1:
        return 1
    else:
        print(f'calculating {n}!')
        return n * factorial(n-1)

factorial(3)
factorial(3)

cache = {}
def factorial_caching(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        print(f'cached {n}!')
        return cache[n]
    else:
        print(f'calculating {n}!')
        result = n * factorial_caching(n-1, cache=cache)
        cache[n] = result
        return result

print('\nImproved caching example')
factorial_caching(3,cache=cache)
factorial_caching(3,cache=cache)

def factorial_caching(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        print(f'cached {n}!')
        return cache[n]
    else:
        print(f'calculating {n}!')
        result = n * factorial_caching(n-1, cache=cache)
        cache[n] = result
        return result

print('This technique is superior because the code is more concise and the user does not have to worry about providing a cache')
print('\nImproved caching example -- default cache')
factorial_caching(10)
factorial_caching(10)
new_cache = {}
print('\nImproved caching example -- user-provided cache')
factorial_caching(10, cache=new_cache)
factorial_caching(10, cache=new_cache)

print('Note: using decorators and closures is an even better approach')