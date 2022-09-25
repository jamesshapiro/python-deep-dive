"""
* args

Recall also: a, b, *c = 10, 20, 'a', 'b'
          -> a = 10, b = 20, c = ['a', 'b']

Something similar happens when positional arguments are passed to a function

def func_1(a, b, *c):
    # code

Note that c gets unpacked into a tuple instead of a list

The * parameter name is arbitrary, you can make it whatever you want

It is customary, but not required, to name it *args

Note: you cannot add more positional arguments after *args
"""

def func_1(a, b, *c):
    print(f'{a=}, {b=}, {c=}')
    print(f'{type(c)=}')

func_1(10,20,'a','b')
func_1(10,20,30,'b')
func_1(10,20)

def func_1(a, b, *args):
    print(f'{a=}, {b=}, {c=}')

def bad_func(a, b, *args, d):
    print(f'{a=}, {b=}, {c=}, {d=}')

try:
    bad_func(10, 20, 30, 40, 50)
except TypeError as e:
    print(e)

"""Unpacking arguments

Suppose we have our function:

def func1(a,b,c):
    print(f'{a=}, {b=}, {c=}')

And a list of arguments:
l = [10,20,30]

And we want to pass the arguments into the function

We do so as follows:
"""

def func1(a,b,c):
    print('\nUnpacking arguments example:')
    print(f'{a=}, {b=}, {c=}')

l = [10,20,30]
func1(*l)

def avg(*args):
    return len(args) and sum(args)/len(args)

print(f'{avg()=}')
print(f'{avg(1,2)=}')
print(f'{avg(1,2,3)=}')
print(f'{1 and 2=}')
print(f'{1 and 7777777=}')
print(f'{7777777777777777777777 and 777=}')
print(f'{0 and 777=}')

print('\nAvg requiring 1+ argument')
def avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total / a

print(f'{avg(1,2)=}')
print(f'{avg(1,2,3)=}')
try:
    print(f'{avg()=}')
except TypeError as e:
    print(e)

l = [10,20,30,40,50]

def func1(a,b,c,*args):
    print(f'{a=}, {b=}, {c=}, {args=}')

func1(*l)
