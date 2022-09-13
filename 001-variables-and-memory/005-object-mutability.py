print('''changing the data inside an object is called
"modifying the internal state" of the object.
The object was "mutated". An object whose internal
state can be changed is called "Mutable". An object
whose internal state *cannot* be changed is called
immutable.
''')

print('''examples of immutable objects:
- Numbers (int, float, Booleans, etc.)
- Strings
- Tuples
- Frozen Sets
- User-Defined Classes that do not have a way to mutate state''')

print('''examples of mutable objects:
- Lists
- Sets
- Dictionaries
- User-Defined Classes that let you mutate state
''')

print('A slightly tricky mutability example:')

print('a = [1,2]')
print('b = [3,4]')
print('t = (a,b)')
a = [1,2]
b = [3,4]
t = (a,b)
print(f'{t=}')
a.append(3)
b.append(5)
print('a.append(3)')
print('b.append(5)')
print(f'{t=}')

print('''\nThe lesson is that objects are only immutable
if every object they contain is also immutable''')

print('\nmy_list = [1,2,3]')
my_list = [1,2,3]
print(f'{hex(id(my_list))=}')
print('my_list.append(4)')
my_list.append(4)
print(f'{hex(id(my_list))=}')

print('\nother_list = [1,2,3]')
other_list = [1,2,3]
print(f'{hex(id(other_list))=}')
print('other_list = other_list + [4]')
print('This changes where the list points to!!')
other_list = other_list + [4]
print(f'{hex(id(other_list))=}')

print('''\nThe "append" method modifies the internal
state of a list. By contrast, other_list + [4]
concatenates two lists and returns a new list''')

print("my_dict = dict(key_1=1, key_2=2)")
my_dict = dict(key_1=1, key_2=2)
print(f'{my_dict=}')
print(f'{hex(id(my_dict))=}')
print("my_dict['key_3'] = 3")
my_dict['key_3'] = 2.5
print(f'{hex(id(my_dict))=}\n')

print('t = (1,2,3)')
t = (1,2,3)
print(f'{hex(id(t))=}')
print(f'{hex(id(t[0]))=}')
print(f'{hex(id(t[1]))=}')

print('\nt = ([1,2],[3,4])')
t = ([1,2],[3,4])
print(f'{hex(id(t))=}')
print(f'{hex(id(t[0]))=}')
print(f'{hex(id(t[1]))=}')
print('t[0].append(5)')
t[0].append(5)
print(f'{hex(id(t))=}')
print(f'{hex(id(t[0]))=}')
print(f'{t=}')