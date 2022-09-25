"""
Keyword Arguments

Recall that positional parameters can, optionally, be passed as named (keyword) arguments
"""

def func(a,b,c):
    print(f'{a=}, {b=}, {c=}')

func(1,2,3)
func(b=1,c=2,a=3)

"""
Using named arguments in this case is entirely up to the caller

Mandatory Keyword Arguments:

We can make keyword arguments mandatory

To do so, we create parameters after the positonal parameters have been exhausted
"""

def func(a,b,*args,d):
    print(f'{a=}, {b=}, {args=}, {d=}')

func(1,2,'x','y','z',d=100)
func(1,2,d=100)
try:
    func(1,2)
except TypeError as e:
    print(e)

print('\nWe can even omit any mandatory positional arguments as follows:')
def func(*args,d):
    print(f'{args=}, {d=}')

func(1,2,d=100)
func(d=100)

print('\nWe can also force NO positional arguments as follows:')
def func(*,d):
    print(f'{d=}')

try:
    func(1,2,d=100)
except TypeError as e:
    print(e)

try:
    func(100)
except TypeError as e:
    print(e)

func(d=100)

"""
Putting it together

def func_1(a,b=1,*args,d,e=True):
    print(f'{a=}, {b=}, {args=}, {d=}, {e=}')

def func_2(a,b=1,*,d,e=True):
    print(f'{a=}, {b=}, {args=}, {d=}, {e=}')

a: mandatory positional argument (may be specified with a named argument)
b: optional positional argument (may be specified postionally, or as a named argument,
   or not at all), defaults to 1
args: catch-all for any (optional) additional positional arguments
*:    no additional positional arguments allowed
d: mandatory keyword argument (must be specified with a named argument)
e: optional keyword argument (optional keyword argument), defaults to True
"""

def func1(a,b,*,d):
    print(f'{a=}, {b=}, {d=}')

try:
    func1(1,2,3,d=4)
except TypeError as e:
    print(e)

func1(1,2,d=4)

def func1(a,b=1,*args,d):
    print(f'{a=}, {b=}, {args=}, {d=}')

func1(1,2,3,4,d=5)


def func1(a,b=1,*args,d=0,e):
    print(f'{a=}, {b=}, {args=}, {d=}, {e=}')

note = """
NOTE: unlike with positional arguments, you can have optional
keyword arguments (with a default value provide) come BEFORE
mandatory keyword arguments!!!
This is because keyword arguments are always specified with a name
so there is no potential ambiguity
"""
print(note)

func1(1,2,3,4,e=1)

try:
    func1(1,2,3,4,1)
except TypeError as e:
    print(e)

func1(0,600,d='Shalom World',e=10.0)
func1(11,'m/s', 24, 'mph', d='circle', e='square')