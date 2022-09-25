"""
Recap:

positional arguments
- specific
- may have default values

*args
- collects, and exhausts, remaining positional arguments

*
- indicates the end of positional arguments (effectively exhausts)

keyword-only arguments
- *must* be passed as a key-value pair
- note that positonal arguments *may optionally* be passed as a k-v pair
- after positional arguments have been exhausted
- specific
- may have default values

**kwargs
- collects into a dictionary any extra keyword arguments that it finds

a, b, c=10, *args / *, kw1, kw2=100, **kwargs

a -> positional argument
b -> positional argument
c -> optional positional argument with default value
*args / * -> remaining positional arguments (or end of positional arguments)
kw1 -> keyword argument
kw2 -> optional keyword argument with default value
kwargs -> remaining keyword arguments

Often keyword-only arguments are used to modify the default behavior of a function
"""

def func1(a,b,*args):
    print(f'{a=},{b=},{args=}')

func1(1,2,'x','y','z')

note = """
NOTE: You can't actually invoke the function with positional arguments before *args
"""

# throws SyntaxError: positional argument follows keyword argument
# func1(a=3,b=4,'x','y','z')

def func1(a,b=2,c=3,*args):
    print(f'{a=},{b=},{c=},{args=}')

func1(5,c=5)
# throws SyntaxError: positional argument follows keyword argument
# func1(5,c=5,'x','y','z')

print('So once you start using *args you kind of lose the ability to set default positional arguments (see above)')

def func1(a,b=2,*args,c=3,d):
    print(f'{a=},{b=},{args=},{c=},{d=}')

func1(10,20,'x','y','z',c=4,d=1)
func1(10,20,'x','y','z',d=10)
try:
    func1(1,'x','y','z',b=4,d=10)
except TypeError as e:
    print(e)
print('So use keyword args with default values if you want to use default values in a function with *args')

def func1(a,b,*args,c=10,d=20,**kwargs):
    print(f'{a=},{b=},{args=},{c=},{d=},{kwargs=}')

func1(1,2,'x','y','z',c=100,d=200,x=0.1,y=0.2)

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo)/2
    if log_to_console:
        print(f'high={hi}, low={lo}, avg={avg}')
    return avg

is_debug = True
avg = calc_hi_lo_avg(1,2,3,100,log_to_console=is_debug)