import ctypes
import gc

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

note = """
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value
"""
print(note)

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"

print('\n(1.) Circular references example:')

class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: self: {hex(id(self))}, b: {hex(id(self.b))}')

class B:
    def __init__(self, a):
        self.a = a
        print(f'B: self: {hex(id(self))}, a: {hex(id(self.a))}')

gc.disable()

my_var = A()

# hypothesis: I predict the value of this is hex(id(my_var.b.a))
print(f'{hex(id(my_var))=}')
print(f'{hex(id(my_var.b.a))=}')

a_id = id(my_var)
b_id = id(my_var.b)

note = """
Note: what follows is as expected. my_var initially points to a, 
and a.b also points to a. a also points to b.

After my_var is set to None, the circular reference remains.
"""
print(note)

print(f'{ref_count(a_id)=}')
print(f'{ref_count(b_id)=}')
print(f'{object_by_id(a_id)=}')
print(f'{object_by_id(b_id)=}')

print('\nmy_var = None')
my_var = None

print(f'{ref_count(a_id)=}')
print(f'{ref_count(b_id)=}')
print(f'{object_by_id(a_id)=}')
print(f'{object_by_id(b_id)=}')

print('\ngc.collect()')
gc.collect()

note = """
Note: the values for ref_count here are unpredictable as the
memory has been freed
"""

print(note)
print(f'{ref_count(a_id)=}')
print(f'{ref_count(b_id)=}')
print(f'{object_by_id(a_id)=}')
print(f'{object_by_id(b_id)=}')
