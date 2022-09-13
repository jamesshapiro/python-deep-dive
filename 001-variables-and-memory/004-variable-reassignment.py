print('int behavior:\n')

print('a = 10')
a = 10
print(f'{hex(id(a))=}')

type(a)

print('a = 15')
a = 15

print(f'{hex(id(a))=}')

print('a = a + 1')
a = a + 1

print(f'{hex(id(a))=}')

print('a = 10')
print('b = 10')
a = 10
b = 10
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')

