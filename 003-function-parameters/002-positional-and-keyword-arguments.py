"""
Positional arguments:

Most common way of assigning arguments to parameters: via the order in which they are passed
i.e. their *position*

def my_func(a, b):
    # code

my_func(10, 20)   -> a = 10, b = 20
my_func(20, 10)   -> a = 20, b = 10

Default Values:
A positional argument can be made optional by specifying a default value for the
corresponding parameter

def my_func(a, b=100):
    # code

my_func(10, 20)   -> a = 10, b = 20
my_func(5)        -> a = 5,  b = 100, default value is used

Default arguments must occur after all non-default arguments:

# This doesn't work (try uncommenting and running):
def my_func(a, b=100, c):
    pass

Keyword Arguments:
Positional arguments can, optionally, be specified by using the parameter name
whether or not the parameters have default values

Once you use a named argument, all arguments thereafter must be named too
"""

def my_func(a, b=5, c=10):
    print(f'{a=}, {b=}, {c=}')

my_func(10)
my_func(10,20)
my_func(10,20,30)
my_func(10,c=15)

def my_func(a, b, c):
    print(f'{a=}, {b=}, {c=}')

my_func(c=30, b=20, a=10)