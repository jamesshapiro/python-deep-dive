""" From the last lecture """

from html import escape

# def htmlize(arg):
#     registry = {
#         object: html_escape,
#         int: html_int,
#         float: html_real,
#         Decimal: html_real,
#         str: html_str,
#         list: html_list,
#         tuple: html_list,
#         dict: html_dict,
#         set: html_set
#     }
#     fn = registry.get(type(arg), registry[object])
#     return fn(arg)

# print()
# print(f'{htmlize(100)=}')
# print(f'{htmlize([1,2,3])=}')

""" Take one """

def singledispatch(fn):
    registry = {}

    registry[object] = fn
    
    def inner(arg):
        return registry[object](arg)
    
    return inner

@singledispatch
def htmlize(a):
    return escape(str(a))

print(f'{htmlize("1 < 100")=}')

""" Take two """

def singledispatch(fn):
    registry = {}

    registry[object] = fn
    registry[int] = lambda a: f'{a}(<i>{str(hex(a))}</i>)'
    registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')
    
    def inner(arg):
        return registry.get(type(arg), registry[object])(arg)

    return inner

@singledispatch
def htmlize(a):
    return escape(str(a))

print(f'{htmlize("1 < 100")=}')
print(f'{htmlize(100)=}')

""" We want something fully generic. Take three: """

def singledispatch(fn):
    registry = {}

    registry[object] = fn
    
    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

print(f'{htmlize("1 < 100")=}')

""" But with the above there is no way to register new types. Take four: """

def singledispatch(fn):
    registry = {}

    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    def dispatch(type_):
        return registry.get(type_, registry[object])
    
    decorated.register = register
    decorated.dispatch = dispatch
    # decorated.registry = registry
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

print(f'{htmlize("1 < 100")=}')
print(f'{htmlize(100)=}')

print(f'{htmlize.register=}')

@htmlize.register(int)
def html_int(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

print(f'{htmlize(100)=}')

@htmlize.register(list)
def html_list(l):
    items = (f'<li>{htmlize(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# Same as html_list = htmlize.register(list)(html_list)
print(f'{htmlize([1,2,3])=}')

# Could also stack them

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = (f'<li>{htmlize(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(f'{htmlize([1,2,3])=}')
print(f'{htmlize((1,2,3))=}')
# print(f'{htmlize.registry=}')
print(f'{htmlize.dispatch(int)=}')

""" This is a good start, but runs into problems with generics """

from numbers import Integral
print(f'{isinstance(100, Integral)=}')

class Person:
    pass

class Student(Person):
    pass

p = Student()

print(f'{type(p)=}')
print(f'{isinstance(p, Student)=}')
print(f'{isinstance(p, Person)=}')

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def html_integral_number(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

print(f'{isinstance(10, Integral)=}')
print(f'{isinstance(True, Integral)=}')

""" Because we are looking at only type, this fails to htmlize correctly """
print(f'{htmlize(10)=}')

@htmlize.register(int)
@htmlize.register(bool)
def html_integral_number(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

print(f'{htmlize(10)=}')

from collections.abc import Sequence

print(f'{isinstance([1,2,3], Sequence)=}')
print(f'{isinstance((1,2,3), Sequence)=}')

@htmlize.register(Sequence)
def html_sequence(l):
    items = (f'<li>{htmlize(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(f'{type([1,2,3]) is Sequence=}')