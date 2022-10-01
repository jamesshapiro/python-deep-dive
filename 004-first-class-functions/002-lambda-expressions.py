"""
What are Lambda Expressions?

We already know how to create functions using the def statement

Lambda expressiosn are simply another way to create functions (anonymous functions)

lambda [parameter list]: expression
  - the parameter list is optional (there can be zero arguments)
  - the ":" is required, even for zero arguments
  - this expression is evaluated and returned when the lambda function is *called*
    think of it as the "body" of the function
  - the entire expression (from "lambda" keyword to end-of-line) returns a *function object*

This whole expression can be assigned to a variable, passed as an argument to a function, etc.
However, unlike functions created with "def", it does not have a name. Hence, "anonymous function"
"""

# Examples:
lambda x: x**2
lambda x, y: x+y
lambda : 'hello'
lambda s: s[::-1].upper()

print(f'{type(lambda x: x**2)=}')

"""
Note: Lambdas, or anonymous functions, are NOT equivalent to closures
"""

my_func = lambda x: x**2
print(f'{my_func(10)=}')

print(f'{type(my_func)=}')

# identical to:
def my_func(x):
    return x**2

print(f'{type(my_func)=}')

"""
Passing as an argument to another Function
"""

def apply_func(x, fn):
    return fn(x)

print(f'{apply_func(3, lambda x: x**2)=}')
print(f'{apply_func(2, lambda x: x+5)=}')
print(f'{apply_func("abc", lambda x: x[1:]*3)=}')

# equivalently
def fn_1(x):
    return x[1:] * 3
apply_func("abc", fn_1)

fn_2 = fn_1
fn_2("abc")
"""
Limitations:

The "body" of a lambda is limited to a single expression

no assignments:    x**lambda x: x = 5**
                   x**lambda x: x = x + 5**
no annotations:    x**lambda x:int : x*2**

single logical line of code -> line-continuation is okay, but still just one expression
"""

# lambda with default values
g = lambda x,y=10: x*y
print(f'{g(1)=}')
print(f'{g(1,2)=}')

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

try:
    f()
except TypeError as e:
    print(e)

print(f'{f(1,y=2)=}')
print(f"{f(1,'a','b',y=2, a=20, b=30)=}")

f = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
print(f"{f(1,'a','b',y=2, a=20, b=30)=}")

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

#print(f'{=}')
sq = lambda x: x**2
print(f'{apply_func(sq,3)=}')
print(f'{apply_func(lambda x: x**2,3)=}')
print(f'{apply_func(lambda x,y: x+y,3,4)=}')
try:
    print(f'{apply_func(lambda x,*,y: x+y,3,50)=}')
except TypeError as e:
    print(e)
print(f'{apply_func(lambda x,*,y: x+y,3,y=100)=}')

print(f'{apply_func(lambda *args: sum(args),1,2,3,4,5)=}')
print(f'{apply_func(sum,[1,2,3,4,5])=}')
print(f'{sum([1,2,3,4,5])=}')

"""
Lambda and Sorting
"""