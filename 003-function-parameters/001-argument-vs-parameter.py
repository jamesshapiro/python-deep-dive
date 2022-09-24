# Mostly semantics

def my_func(a, b):
    note = f"""Function Scope
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""
    print(note)

"""
In this context, a and b are called parameters of my_func
Also note that a and b are variables, local to my_func
"""

x = 10
y = 'a'
my_func(x,y)

"""
In this context, x and y are called the arguments of my_func
Also note that x and y are passed by reference, i.e. the
memory addresses of x and y are what gets passed
"""


note = f"""Module Scope
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         x        +  {hex(id(x))}  +
+         y        +  {hex(id(y))}  +
+++++++++++++++++++++++++++++++++++++++
"""
print(note)

my_func(x, y)