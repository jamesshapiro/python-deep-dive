import sys
import ctypes

value = 12345678

print('(1.) Simple int reference counting example:')
print(f'\n{value=}')
print(f'{sys.getrefcount(value)=}')

a = value
print(f'a = {value}')

print(f'{sys.getrefcount(value)=}')

b = a
print('b = a')
print(f'{sys.getrefcount(value)=}')

a = 11
print('a = 11')
print(f'{sys.getrefcount(value)=}')

b = a
print('b = a')
print(f'{sys.getrefcount(value)=}')

#===============================

# ctypes.c_long.from_address(address).value

print('\n(2.) Simple list reference counting example:')

print('\na = [1,2,3]')
a = [1,2,3]

note = """
Note: invoking sys.getrefcount(a) with argument 'a'
ITSELF creates a new reference to a, hence why sys.getrefcount
'inflates' what we intuitively expect the count to be. We
can use the ctypes function below to get the truly accurate
count.
"""
print(note)
print(f'{sys.getrefcount(a)=}')
print(f'{ctypes.c_long.from_address(id(a)).value=}')

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

note = """
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

Note: id does create a new reference to a, but by the
time it returns the address for a, that reference gets
destroyed, hence why the reference count is still
accurate.
"""
print(note)
print('\nstored_address = id(a)')
stored_address = id(a)
print(f'{ref_count(stored_address)=}')

print('\nb = a')
b = a
print(f'{ref_count(stored_address)=}')

print('\nb = None')
b = None
print(f'{ref_count(stored_address)=}')

print('a = None')
a = None

note = """
Note: we can get unpredictable results after
setting a to None, because at that point, c
frees up the memory. However, when I tested
this out the ref_count went to 0 as desired
"""
print(note)
print(f'{ref_count(stored_address)=}')
