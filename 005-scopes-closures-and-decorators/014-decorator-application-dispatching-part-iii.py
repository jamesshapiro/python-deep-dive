"""
What we did in the last lesson is good, but doesn't work for
inheritance. So, for example, it breaks for Sequence, Integral,
etc.

However, Python has a built-in function that does this for us:
"""

from functools import singledispatch

from numbers import Integral
from collections.abc import Sequence
from html import escape

@singledispatch
def htmlize(a):
    return escape(str(a))

print(f'{htmlize.registry=}')
print(f'{htmlize.dispatch(str)=}')

@htmlize.register(Integral)
def htmlize_integral_number(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

print()
print(f'{htmlize.registry=}')
print(f'{htmlize.dispatch(int)=}')
print(f'{type(int)=}')
print(f'{isinstance(10, int)=}')
print(f'{isinstance(10, Integral)=}')

print()

print(f'{isinstance(True, Integral)=}')
print(f'{htmlize.dispatch(bool)=}')
print(f'{type(bool)=}')
print(f'{htmlize(True)=}')

@htmlize.register(Sequence)
def html_sequence(l):
    items = (f'<li>{htmlize(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print()
print(f'{htmlize([1,2,3])=}')
print(f'{htmlize((1,2,3))=}')
print(f'{isinstance("python", Sequence)=}')
print('htmlize("python")')
try:
    print(f'{htmlize("python")=}')
except RecursionError:
    print("RecursionError")

@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br>\n')

print(f'{htmlize("python. 1 < 100")=}')

@htmlize.register(tuple)
def html_tuple(t):
    items = (escape(str(item)) for item in t)
    return f'({", ".join(items)})'

print(f'{htmlize.registry=}')
print(f'{htmlize((1,2,3))=}')
print(f'{htmlize([1,2,3])=}')

""" Often instead of explicitly naming the function, people write an underscore
to emphasize that the function is not meant to be called directly. """

