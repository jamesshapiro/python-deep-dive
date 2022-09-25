"""
**kwargs

*args is used to scoop up a variable number of remaining positional arguments -> tuple
      The parameter name args is arbitrary - * is the real performer here

**kwargs is used to scoop of a variable number of remaining keyword arguments -> dictionary
      The parameter name kwargs is arbitrary - * is the real performer here

**kwargs can be specified even if the positional arguments have NOT been exhausted,
      UNLIKE keyword only arguments

However, no parameters can come after **kwargs

Example:
"""

def func1(*,d,**kwargs):
      print(f'{d=},{kwargs=}')

func1(d=1, a=2, b=3)
func1(a=1, d=2, b=3)
func1(d=1)

def func1(**kwargs):
      print(f'{kwargs=}')

func1()

def func1(*args, **kwargs):
      print(f'{args=}, {kwargs=}')

func1(1,2,a=10,b=20)
func1()

# Yields "positional arguments" cannot appear after keyword arguments SyntaxError
# func1(z='shalom world',1,2,a=10,b=20)

print('\nSuppose you want a named argument before kwargs after exactly two positional arguments:')
def func1(a,b,*,d,**kwargs):
      print(f'{a=}, {b=}, {d=}, {kwargs=}')

func1(1,2,d=10,e=20,f=30)

def func1(a,b,**kwargs):
      print(f'{a=}, {b=}, {kwargs=}')

try:
      func1(1,2,3,e=20,f=30)
except TypeError as e:
      print(e)

func1(1,2,e=20,f=30)