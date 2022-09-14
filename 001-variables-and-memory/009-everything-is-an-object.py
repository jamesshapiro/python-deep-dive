"""
Everything in Python is an object (i.e. an instance of a class)
- Functions
- Classes (class) [not just the instances, but the class itself]
- Types (type)

This means they all have a memory address!

After declaring:

def my_func():
    ...

my_func is a variable that points to an object

Hence:

Any object can be assigned to a variable (including functions)
Any object can be passed to a function (including functions)
Any object can be returned from a function (including functions)
"""

a = 10
print(f'{type(a)=}')
b = int(10)
print(f'{type(b)=}')

# The "help" function gives you built in documentation for
# a type
#help(int)

def square(a):
    return a ** 2

print(type(square))

f = square

print(hex(id(square)))

print(f is square)
print(f'{f(2)=}')

def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(f'{f is square=}')

print(f'{select_function(1)(2)=}')
print(f'{select_function(500)(2)=}')

def exec_function(fn, n):
    return fn(n)

print(f'{exec_function(cube, 3)=}')

