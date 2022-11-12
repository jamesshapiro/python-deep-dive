"""
Decorator Application - Decorator Class
"""

def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: {a=}, {b=}')
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print(f'Hello {s}')

my_func('World')

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, c):
        print("called {self.a=} {self.b=} {c=}")

obj = MyClass(10, 20)

print(f'{obj=}')
print(f'{obj.__call__(100)=}')
print(f'{obj(100)=}')

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f"decorated function called with {self.a=} {self.b=}")
            return fn(*args, **kwargs)
        return inner

print('\nWith class decorator:')

@MyClass(10, 20)
def my_func(s):
    print(f'Hello {s}')

print(f'{my_func("World")=}')

print('\nEquivalently...')
obj = MyClass(10, 20)

def my_func(s):
    print(f'Hello {s}')

my_func = obj(my_func)
print(f'{my_func("World")=}')

print('\nEquivalently again...')

def my_func(s):
    print(f'Hello {s}')
my_func = MyClass(10, 20)(my_func)
print(f'{my_func("World")=}')