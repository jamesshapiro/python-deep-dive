# earlier we saw that 
a = 10
b = 10
print(f'{a is b=}')

print('''Note: if you run this after compiling as a script, Python will
tend to optimize all numbers to a single address, no matter how large
but if you run this interactively, it will not''')
a = 500
b = 500
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{a is b=}')

"""
At startup, Python (CPython), pre-loads (caches) a global list of integers
in the range [-5, 256]
Any time an integer in that range is referenced, Python will use the cached
version of that object

Whenever you want to set a variable to 10, Python just looks up the address
for 10. It is a singleton.

Some string are also automatically interned, but not all
As the Python code is compiled, identifiers are interned

Identifiers include:
- variable names
- function names
- class names
- etc.

Identifiers:
- must start with _ or a letter
- can only contain _, letters and numbers

Some string literals may also be automatically interned:
- string literals that look like identifiers (e.g. "hello_world")
- but don't count on it

Why does Pytohn do this?
- Speed and memory optimization
- Python both internally and in the code you write deals with tons
  of dictionary type lookups on string keys, which means tons of
  string equality testing

a = 'some_long_string'
b = 'some_long_string'

Checking if the strings are equal is near instant if you just
have to compare memory addresses

You can force strings to be interned by using the sys.intern() method

import sys
a = sys.intern('the quick brown fox')
b = sys.intern('the quick brown fox')
a is b

When should you do this?
- Dealing with a huge number of strings that could have high repetition
  e.g. tokening a large corpus of text (NLP)
"""

print('NOTE: TRY TO RUN ALL OF THESE EXAMPLES INTERACTIVELY, NOT AS A SCRIPT')
a = 'hello'
b = 'hello'
print(a is b)

a = 'hello world'
b = 'hello world'
print(a is b)

import sys
a = sys.intern('hello world')
b = 'hello world'

print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')

def compare_with_equals(n):
    a = 'a long string that is not interned. ' * 200
    b = 'a long string that is not interned. ' * 200
    for i in range(n):
        if a == b:
            pass

def compare_with_interning(n):
    a = sys.intern('a long string that is not interned. ' * 200)
    b = sys.intern('a long string that is not interned. ' * 200)
    for i in range(n):
        if a is b:
            pass

import time

start = time.perf_counter()
compare_with_equals(10_000_000)
end = time.perf_counter()
print(f'equality: {end-start}')


start = time.perf_counter()
compare_with_interning(10_000_000)
end = time.perf_counter()
print(f'interning: {end-start}')

print('so consider interning if you are doing millions of string comparisons')