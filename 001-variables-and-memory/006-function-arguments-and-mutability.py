my_var = 'hello'

# the only way to modify the "value" of my_var is to reassign
# my_var to another object

print('Immutable objects are safe from unintended side effects:')

note = """
def process(s):
    s = s + ' world'
    return s

s = 'shalom'
process(s)
"""

print(note)

def process(s):
    s = s + ' world'
    return s

s = 'shalom'
process(s)
print(f'{s=}')

print('\nMutable objects are NOT safe from unintended side effects:')

note = """
def process(lst):
    lst.append(100)
    return lst

lst = [1,2,3]
process(lst)
"""
print(note)

def process(lst):
    lst.append(100)
    return lst

lst = [1,2,3]
process(lst)
print(f'{lst=}')


print('''\nImmutable objects that CONTAIN mutable objects are 
also NOT safe from unintended side effects:''')

note = """
def process(t):
    t[0].append(3)

t = ([1,2], 'a')

process(t)
"""
print(note)

def process(t):
    t[0].append(3)

t = ([1,2], 'a')

process(t)
print(f'{t=}')

print('\nMore in-depth string example:\n')

def process(s):
    print(f'Initial s #: {hex(id(s))=}')
    s = s + ' world'
    print(f'Final s #: {hex(id(s))=}')

my_var = 'shalom'
print(f'{my_var=}')
print(f'my_var #: {hex(id(my_var))=}')
process(my_var)
print(f'my_var #: {hex(id(my_var))=}')
print(f'{my_var=}')

print('\nMore in-depth list example:\n')

def modify_list(lst):
    print(f'Initial lst #: {hex(id(lst))=}')
    lst.append(100)
    print(f'Final lst #: {hex(id(lst))=}')

my_list = [1, 2, 3]
print(f'{my_list=}')
print(f'my_list #: {hex(id(my_list))=}')
modify_list(my_list)
print(f'my_list #: {hex(id(my_list))=}')
print(f'{my_list=}')

print('\nMore in-depth tuple example:\n')

def modify_tuple(t):
    print(f'Initial t #: {hex(id(t))=}')
    t[0].append(100)
    print(f'Final t #: {hex(id(t))=}')

my_tuple = ([1, 2], 'a')
print(f'{my_tuple=}')
print(f'my_tuple #: {hex(id(my_tuple))=}')
modify_tuple(my_tuple)
print(f'my_tuple #: {hex(id(my_tuple))=}')
print(f'{my_tuple=}')