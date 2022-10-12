"""
Reducing Function Arguments
"""

def my_func(a,b,c):
    print(a,b,c)

def fn(b,c):
    return my_func(10,b,c)

f = lambda b,c: my_func(10,b,c)

fn(20,30)
f(20,30)

from functools import partial

f = partial(my_func, 10)
f(20,30)

"""
Handling more complex arguments
"""

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a,b,args,k1,k2,kwargs)

def f(b,*args,k2,**kwargs):
    return my_func(10,b,*args,k1='a',k2=k2,**kwargs)

def pow(base, exponent):
    return base ** exponent

square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)

print(f'{square(5)=}')
print(f'{cube(5)=}')
print('But beware:')
print(f'{square(5, exponent=3)=}')

"""
Also beware:
You can use variables when creating partials but there arises a 
similar issue to argument default values
"""
def my_func(a,b,c):
    print(a,b,c)

a = 10
f = partial(my_func, a)
f(20,30)
a = 100
f(20,30)
f = partial(my_func, 10, 11)
f(30)

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a,b,args,k1,k2,kwargs)

my_func(10,20,100,200,k1='a',k2='b',k3=1000,k4=2000)

def f(x, *vars, kw, **kwvars):
    return my_func(10,x,*vars,k1='a',k2=kw,**kwvars)

f(20,100,200,kw='b',k3=1000,k4=2000)

f = partial(my_func,10,k1='a')
f(20,100,200,k2='b',k3=1000,k4=2000)

def my_func(a,b):
    print(a,b)

print('\nPartial example with mutable arguments on definition:')
a = [1,2]
f = partial(my_func, a)
f(100)
a.append(3)
f(100)

"""
Applications:
"""

origin = (0,0)
l = [(1,1), (0,2), (-3,2), (0,0), (10,10)]
dist2 = lambda a, b: (a[0] - b[0])**2 + (a[1]-b[1])**2
print(f'{dist2((1,1), origin)=}')
print(f'{sorted(l, key=lambda x: dist2(x, origin))=}')

print(f'{sorted(l, key=partial(dist2, origin))=}')

f = partial(dist2, origin)
print(f'{sorted(l, key=f)=}')

