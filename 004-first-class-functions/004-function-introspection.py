"""
Functions are first-class objects

They have attributes, e.g.: __doc__, __annotations__

We can attach our own attributes:
"""
#print(f'{=}')

def my_func(a,b):
    return a + b

my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(f'{my_func.category=}')
print(f'{my_func.sub_category=}')

"""
The dir() function

dir() is a built-in functin that, given an object as an argument, will return a list
of valid attributes for that object
"""

print(f'{dir(my_func)=}')

"""
Function Attributes: __name__, __defaults__, __kwdefaults__

__name__       -> name of function
__defaults__   -> tuple containing positional parameter defaults
__kwdefaults__ -> dictionary containing keyword-only parameter defaults
"""
def my_func(a,b=2,c=3,*,kw1,kw2=2):
    pass

print(f'{my_func.__name__=}')
print(f'{my_func.__defaults__=}')
print(f'{my_func.__kwdefaults__=}')
print(f'{my_func.__code__=}')

def my_func(a,b=1,*args,**kwargs):
    i = 10
    b = min(i, b)
    return a * b

print(f'{my_func.__code__.co_varnames=}')
print(f'{my_func.__code__.co_argcount=}')

"""
The inspect Module
import inspect

ismethod(obj) isfunction(obj) isroutine(obj) and many others

- What's the difference between a function and a method?

Classes and objects have attributes - an object that is bound (to the class or the object)
An attribute that is callable, is called a method

def my_func():
    pass

def MyClass:
    def func(self):
        pass

my_obj = MyClass

func is bound to my_obj, an instance of MyClass
isfunction(my_func) -> True
ismethod(my_func) -> False
isfunction(my_obj.func) -> False
ismethod(my_obj.func) -> True
"""


import inspect

def my_func():
    pass

class MyClass:
    def func(self):
        pass

my_obj = MyClass()

print(f'{inspect.isfunction(my_func)=}')
print(f'{inspect.ismethod(my_func)=}')
print(f'{inspect.isfunction(my_obj.func)=}')
print(f'{inspect.ismethod(my_obj.func)=}')
print(f'{inspect.isroutine(my_func)=}')
print(f'{inspect.isroutine(my_obj.func)=}')

"""
Code introspection

We can recover the source code of our functions/methods
inspect.getsource

We can find out which module our function was created in
inspect.getmodule
"""
import math
print(f'{inspect.getsource(my_func)=}')
print(f'{inspect.getmodule(my_func)=}')
print(f'{inspect.getmodule(print)=}')
print(f'{inspect.getmodule(math.sin)=}')

"""
Function Comments
"""
# setting up variable
i = 10

# TODO: Implement function
# some additional notes
def my_func(a, b=1):
    # comment inside my_func
    pass

print(f'{inspect.getcomments(my_func)=}')

"""
Callable Signatures

inspect.signature(my_func) -> Signature instance

Contains an attribute called parameters

Essentially a dictionary of parameter names (keys), and metadata
about the parameters (values)

keys -> parameter name
values -> object with attributes such as name, default, annotation, kind

kind
    POSITIONAL_OR_KEYWORD
    VAR_POSITIONAL
    KEYWORD_ONLY
    VAR_KEYWORD
    POSITIONAL_ONLY

Callable Signatures
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg',
            **kwargs: 'additional keyword-only args') -> str:
    #does something
    #or other
    pass
"""
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg',
            **kwargs: 'additional keyword-only args') -> str:
    #does something
    #or other
    pass
print('\nSignature Example:')
print(f'{inspect.signature(my_func)=}')
print(f'{inspect.signature(my_func).return_annotation=}\n')

#print(f'{=}')

for param in inspect.signature(my_func).parameters.values():
    print(f'Name: {param.name=}')
    print(f'Default: {param.default=}')
    print(f'Annotation: {param.annotation=}')
    print(f'Kind: {param.kind=}\n')

sig = inspect.signature(my_func)
print(f'{sig.parameters=}')
print('iterating signature.parameters:')
print('-'*30)
for k,param in sig.parameters.items():
    print(f'Key: {k}')
    print(f'Name: {param.name=}')
    print(f'Default: {param.default=}')
    print(f'Annotation: {param.annotation=}')
    print(f'Kind: {param.kind=}')
    print('-'*30)

print()

def my_func(a: 'mandatory positional', 
            b: 'optional positional'=1, 
            c=2, 
            *args: 'add extra positional here', 
            kw1, 
            kw2=100, 
            kw=200, 
            **kwargs: 'provide extra kw-only here') -> 'does nothing':
    """This function does nothing but does have various parameters
    and annotations.
    """
    i = 10
    j = 20

print(f'{my_func.__doc__=}')
print(f'{my_func.__annotations__=}')

my_func.short_description = 'this is a function that does nothing much'
print(f'{my_func.short_description=}')
print(f'{dir(my_func)=}')
print(f'{my_func.__name__=}')

def func_call(f):
    print(f'{hex(id(f))=}')
    print(f'{f.__name__=}')
    

func_call(my_func)
print(f'{hex(id(my_func))=}')
print(f'{my_func.__defaults__=}')
print(f'{my_func.__kwdefaults__=}')
print(f'{my_func.__code__=}')
print(f'{dir(my_func.__code__)=}')
print(f'{my_func.__code__.co_varnames=}')
print(f'{my_func.__code__.co_argcount=}')

import inspect
from inspect import isfunction, ismethod, isroutine
a = 10
print(f'{isfunction(a)=}')
print(f'{isfunction(lambda : 1)=}')
print(f'{isfunction(my_func)=}')
print(f'{ismethod(my_func)=}')

class MyClass:
    def f(self):
        pass
print(f'{isfunction(MyClass.f)=}')
print(f'{ismethod(MyClass.f)=}')

my_obj = MyClass()
print(f'{isfunction(my_obj.f)=}')
print(f'{ismethod(my_obj.f)=}')


def my_func(a: 'mandatory positional', 
            b: 'optional positional'=1, 
            c=2, 
            *args: 'add extra positional here', 
            kw1, 
            kw2=100, 
            kw=200, 
            **kwargs: 'provide extra kw-only here') -> 'does nothing':
    """This function does nothing but does have various parameters
    and annotations.
    """
    i = 10
    j = 20
    a = i + j
    return a

print(f'{inspect.getsource(my_func)=}')

# this works
divmod(4,3)

# this fails, because these are positional args only
try:
    divmod(x=4,y=3)
except TypeError as e:
    print(e)

print(f'{inspect.signature(divmod)=}')
for param in inspect.signature(divmod).parameters.values():
    print(f'{param.kind=}')
