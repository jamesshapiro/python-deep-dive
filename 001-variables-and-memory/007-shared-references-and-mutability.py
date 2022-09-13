# Python reuses the area of memory that is referenced as an optimization
# because the object is immutable, there is no risk that changes to one
# will mutate the other
print('Shared references and mutability examples: ')

code = """
a = 10
b = 10
"""
print(code)

a = 10
b = 10
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')

code = """
a = 'hello'
b = 'hello'
"""
print(code)

a = 'hello'
b = 'hello'
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')