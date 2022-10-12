"""
What are callables?

Any object that can be claled using the () operator
    callables *always* return a value (that value can be None)

Callables include:
  - functions
  - methods
  - many other objects

To see if an object is callable, we can use the built-in function: callable
"""
print(f'{callable(print)=}')
print(f'{callable("abc".upper)=}')
print(f'{callable("abc".upper())=}')
print(f'{callable("abc")=}')
print(f'{callable(str.upper)=}')
print(f'{callable(callable)=}')
print(f'{callable(10)=}')

"""
Different Types of Callables

  - built-in functions (e.g. print, len, callable)
  - built-in methods (e.g. a_str.upper, a_list.append)
  - user-defined functions (created with def or lambda)
  - methods (functions *bound* to an object)
  - classes (MyClass(x,y,z)):
    -> (1.) calls the "__new__(x,y,z)" method (creates the new object), THEN
    -> (2.) calls the "__init__(self,x,y,z) method, THEN
    -> (3.) returns the object (reference)
  - class instances (if the class implements the "__call__" method)
  - generators, coroutines, asynchronous generators
"""

print('\nAll callables return *something*, whether None or something else')
print(f'{callable(print)=}')
result = print('hello')
print(f'{result=}')
l = [1,2,3]
print(f'{callable(l.append)=}')
result = l.append(4)
print(f'{result=}')
s = 'abc'
print(f'{callable(s.upper)=}')
result = s.upper()
print(f'{result=}')

from decimal import Decimal
print(f'{callable(Decimal)=}')
result = Decimal('10.5')
print(f'{result=}')
print(f'{callable(result)=}')

print('\nCallable classes and class instance examples')
class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x

print(f'{callable(MyClass)=}')
print(f'{callable(MyClass())=}')

class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x
    def __call__(self, x=1):
        print(f'updating counter to {self.counter + x}')
        self.counter += x

print(f'========\n{callable(MyClass)=}')
print(f'{callable(MyClass())=}')
result = MyClass()
MyClass.__call__(result, 10)
result()
result()
