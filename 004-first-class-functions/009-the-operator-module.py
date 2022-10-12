"""
The operator module

Application: use certain simple functions without having to
create a lambda

Arithmetic Functions:
- add(a,b)
- mul(a,b)
- pow(a,b)
- mod(a,b)
- floordiv(a,b)
- neg(a)

Comparison and Boolean Operators:
- lt(a,b)
- gt(a,b)
- eq(a,b)
- le(a,b)
- get(a,b)
- ne(a,b)

Sequence/Mapping Operators:
- concat(s1, s2)
- contains(sequence, value)
- countOf(sequence, value)
- getitem(sequence, index)
- setitem(sequence, index, value)
- delitem(sequence, index)

Item Getters:
The itemgetter function returns a callable

getitem(s, i) takes two parameters, and returns a value: s[i]
"""
import operator

s = [1,2,3]
print(f'{operator.getitem(s, 1)=}')

"""
By contrast, itemgetter is a bit like a partial function
"""

first_item_getter = operator.itemgetter(1)
print(f'{first_item_getter(s)=}')
print(f'{first_item_getter("python")=}')
print(f'{first_item_getter(range(123,456))=}')
print(f'{operator.itemgetter(6)("hello world!")=}')

l = [1,2,3,4,5,6]
s = 'python'
f = operator.itemgetter(1,3,4)
print(f'{f(l)=}')
print(f'{f(s)=}')

"""
Attribute Getters

The attrgetter function is similar to itemgetter, but is used to
retrieve object attributes

It also returns a callable that takes the object as an argument

Suppose my_obj is an object with three properties:

my_obj.a -> 10
my_obj.b -> 20
my_obj.c -> 30

f = operator.attrgetter('a')
f(my_obj) -> 10
f = operator.attrgetter('a', 'c')
f(my_obj) -> (10, 30)

Can also call directly:

  attrgetter('a','b','c')(my_obj)
"""

"""
Calling another Callable

Consider the str class that provides the upper() method:
"""
s = 'python'
print(f'{s.upper()=}')
f = operator.attrgetter('upper')
print(f'{f(s)()=}')
print(f'{operator.attrgetter("upper")(s)()=}')

"""
OR we can use the slightly simpler "methodcaller" function
"""

print(f'{operator.methodcaller("upper")("python")=}')
print(f'{operator.add(1,2)=}')
print(f'{operator.mul(2,3)=}')
print(f'{operator.truediv(3,2)=}')
print(f'{operator.floordiv(13,2)=}')

from functools import reduce
print(f'{reduce(lambda x,y: x*y, [1,2,3,4])=}')
print(f'{reduce(operator.mul, [1,2,3,4])=}')
print(f'{operator.lt(10,3)=}')
print(f'{operator.is_("abc","def")=}')
print(f'{operator.is_("abc","abc")=}')
print(f'{operator.truth([])=}')
print(f'{operator.truth([1])=}')
print(f'{operator.truth([0])=}')
my_list = [1,2,3,4]
print(f'{my_list[1]=}')
print(f'{operator.getitem(my_list, 1)=}')
my_list[1]=100
print(f'{my_list=}')
del my_list[3]
print(f'{my_list=}')
my_list = [1,2,3,4]
print(f'{my_list=}')
operator.setitem(my_list, 1, 100)
print(f'{my_list=}')
operator.delitem(my_list, 3)
print(f'{my_list=}')

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    
    def test(self):
        print('test method running...')

obj = MyClass()
print(f'{type(obj)=}')
print(f'{obj.a=}')
print(f'{obj.b=}')
print(f'{obj.test=}')
print(f'{obj.test()=}')
print(f'{operator.attrgetter("a")(obj)=}')
my_var = 'b'
prop_b_getter = operator.attrgetter(my_var)
print(f'{prop_b_getter(obj)=}')
print(f'{operator.attrgetter("a","b")(obj)=}')
test = operator.attrgetter('test')(obj)
print(f'{test()=}')
f = lambda x: x.a
print(f'{f(obj)=}')
a = 5 + 10j
l = [5-10j, 3+3j, 2-100j]
try:
    sorted(l)
except TypeError as e:
    print(e)

print(f'{sorted(l, key=lambda x: x.real)=}')
print(f'{sorted(l, key=operator.attrgetter("real"))=}')
l = [(2,3,4),(1,3,5),(6,), (4,100)]
print(f'{sorted(l, key=lambda x: x[0])=}')
print(f'{sorted(l, key=operator.itemgetter(0))=}')

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self, c):
        print(f'{self.a} {self.b} {c}')

obj = MyClass()
f = operator.attrgetter('test')

print(f'{f(obj)=}')
print(f'{obj.a=}')
print(f'{obj.test(100)=}')
print(f'{operator.methodcaller("test", 100)(obj)=}')

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self, c, d):
        print(f'{self.a} {self.b} {c} {d}')
obj = MyClass()
print(f'{operator.methodcaller("test", 100, 200)(obj)=}')

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self, c, d, *, e):
        print(f'{self.a} {self.b} {c} {d} {e}')
obj = MyClass()
print(f'{operator.methodcaller("test", 100, 200, e=300)(obj)=}')
f = operator.attrgetter("test")
print(f'{f(obj)(10,20,e=100)=}')
