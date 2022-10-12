"""
High order functions

A function that takes a function as a parameter and/or returns a function as its return value

Example:
  - sorted
  - map
  - filter
"""

"""
The map function

map(func, *iterables)
  - *iterables -> a variable number of iterable objects
  - func       -> some function that takes as many arguments as there are iterable objects passed to iterables

map(func, *iterables) will then return an iterator that calculates the function applied to each element of the iterables

The iterator stops as soon as one of the iterables has been exhausted so unequal length iterables can be used
"""

l = [2,3,4]

def sq(x):
    return x**2

result = list(map(sq, l))
print(f'{result=}')

l1 = [1,2,3]
l2 = [10,20,30]

def add(x,y):
    return x + y

result = list(map(add, l1, l2))

print(f'{result=}')

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50,60,70,80,90]
result = list(map(add, l1, l2))
print(f'{result=}')

"""
The filter function

filter(func, iterable)
  - iterable -> a single iterable
  - func -> some function that takes a single argument

filter(func, iterable) will then return an iterator that contains all the 
elements of the iterable for which the function called on it is Truthy

If the function is None, it simply returns the elements of iterable that are Truthy
"""

l = [-1,0,1,2,3,4]

print(f'{l=}')
print(f'{list(filter(None,l))=}')

def is_even(n):
    return n % 2 == 0

print(f'{list(filter(is_even, l))=}')

"""
The zip function

Technically not a high-order function, but very useful in conjunction with them

zip(*iterables) -> iterable
"""

l1 = (1,2,3,4)
l2 = [10,20,30,40]
l3 = 'abcd'
print(f'{list(zip(l1,l2))=}')
print(f'{list(zip(l1,l2,l3))=}')

l1 = [1]
l2 = [1,2,3,4,5,6,7,8,9,10]
print(f'{list(zip(l1,l2))=}')

"""
List Comprehension Alternative to map
"""

l = [2,3,4]

def sq(x):
    return x**2

print(f'{list(map(sq, l))=}')
print(f'{[x**2 for x in l]=}')

l1 = [1,2,3]
l2 = [10,20,30]

def add(x,y):
    return x + y

result = list(map(lambda x, y: x + y, l1, l2))
print(f'{result=}')
print(f'{[x+y for x,y in zip(l1,l2)]=}')

"""
List Comprehension Alternative to filter
"""
l = [-1,0,1,2,3,4]
print(f'{list(filter(lambda x: x % 2 == 0, l))=}')
print(f'{[x for x in l if x % 2 == 0]=}')

"""
List Comprehension Structure:
[<expression1> for <varname(s)> in <iterable> if <expression2>]
"""

"""
Combining map and filter
"""

l = range(10)
print(f'{list(filter(lambda y: y < 25, map(lambda x: x**2, l)))=}')
print(f'{[x**2 for x in range(10) if x**2 < 25]=}')

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(f'{fact(3)=}')
results = map(fact, range(6))
print('printing all results (1)')
for x in results:
    print(x)
print('printing all results (2)')
for x in results:
    print(x)
print('(map returns a generator)')

l1 = [1,2,3,4,5]
l2 = [10,20,30]
l3 = [100,200,300,400]

print(f'{list(map(lambda x,y,z: x+y+z, l1, l2,l3))=}')

results = map(lambda x,y: x+y, l1, l2,l3)
# error does not show up until here because generators defer computation
try:
    for x in results:
        print(x)
except TypeError as e:
    print(e)

x_range = range(12)
print(f'{x_range=}')
print('printing range (1)')
for i in x_range:
    print(i)
print('printing range (2)')
for i in x_range:
    print(i)
print('so range can be reused while map generators are exhausted on first use')

print(f'{list(filter(lambda x: x%3==0, x_range))=}')
print(f'{[x for x in x_range if x%3==0]=}')
print(f"{list(filter(None, [1,0,4,'a','',None,True,False]))=}")

l1 = [1,2,3,4]
l2 = [10,20,30,40]
l3 = 'python'

results = zip(l1,l2,l3)

print(f'{results=}')
for x in results:
    print(x)

print(f"{list(zip(range(10000), 'python'))=}")
print('iterate zip twice (exhausts after first for-loop)')
result = zip(range(10000), 'python')
for i in result:
    print(i)
for i in result:
    print(i)

print('using generators with comprehensions')

results = (fact(n) for n in range(10))
print(f'{results=}')
print(f'{type(results)=}')

l1 = [1,2,3,4]
l2 = [10,20,30,40,50,60]
print(f'{list(map(lambda x,y: x+y, l1, l2))=}')
print(f'{[x+y for x,y in zip(l1,l2)]=}')
print(f'{list(filter(lambda x: x%2==0,map(lambda x,y: x+y, l1, l2)))=}')
print(f'{[x+y for x,y in zip(l1,l2) if (x+y) % 2 == 0] =}')

