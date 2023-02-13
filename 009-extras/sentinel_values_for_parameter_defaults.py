"""
Sentinel Values for Parameter Defaults

Often we specify the default for a function parameter as None. This allows us to determine
if the user specified an argument for that parameter or not.

There's a potential issue here!

What happens if we need to differentiate between the following:

- a non-None value was provided for the argument
- a None value *was* provided for the argument
- the argument was not provided at all
"""

def validate(a=None):
    if a is not None:
        print('argument was provided')
    else:
        print('argument was NOT provided')

print(f'{validate()=}')
print(f'{validate(1)=}')
print(f'{validate(None)=}')

a = object

print(f'{hex(id(a))}')

_sentinel = object()

def validate(a=_sentinel):
    if a is not _sentinel:
        print('argument was provided')
    else:
        print('argument was NOT provided')
print(f'{validate()=}')
print(f'{validate(1)=}')
print(f'{validate(None)=}')

# alternative method
def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('argument was provided')
    else:
        print('argument was NOT provided')

def validate(a=object(), b=object(), *, kw=object()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_kw = validate.__kwdefaults__['kw']
    if a is not default_a:
        print('argument a was provided')
    else:
        print('argument a was NOT provided')
    if b is not default_b:
        print('argument b was provided')
    else:
        print('argument b was NOT provided')
    if kw is not default_kw:
        print('argument kw was provided')
    else:
        print('argument kw was NOT provided')