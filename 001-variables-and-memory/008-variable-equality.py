# We can think of variable equality in two different ways:

# 1. Same memory address
# 2. Object State (data)

print('Memory address equality example:')
print("\nhello = 'hello'")
print("other_hello = 'hello'")
hello = 'hello'
other_hello = 'hello'
print(f'{hex(id(hello))=}')
print(f'{hex(id(other_hello))=}')
print(f'{hello is other_hello=}')

print('\nObject State (data) equality example:')

print("\nolleh = 'olleh'")
print("other_olleh = 'hello'[::-1]")
olleh = 'olleh'
other_olleh = 'hello'[::-1]
print(f'{hex(id(olleh))=}')
print(f'{hex(id(other_olleh))=}')
print(f'{olleh is other_olleh=}')
print(f'{olleh == other_olleh=}')

print('\nMemory address negation example:')
print(f'{olleh is not other_olleh=}')

print('\nObject State (data) negation example:')
print(f'{olleh != hello=}')

print('\nAnother equality example:')
print('a = [1,2,3]')
print('b = [1,2,3]')
a = [1,2,3]
b = [1,2,3]
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{a is b=}')
print(f'{a == b=}')


print('\nMixed data-type equality example:')
print('a = 10')
print('b = 10.0')
print('c = 10 + 0j')
a = 10
b = 10.0
c = 10 + 0j
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(c))=}')
print(f'{type(c)=}')
print(f'{a is b=}')
print(f'{a == b=}')
print(f'{b == c=}')

print('\nNone example:')
print('a = None')
print('b = None')
print('c = None')
a = None
b = None
c = None
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(c))=}')
print(f'{hex(id(None))=}')
print(f'{type(None)=}')
print(f'{a is b=}')
print(f'{a is None=}')
print(f'{a == None=}')

