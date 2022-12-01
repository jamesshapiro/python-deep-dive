"""
Named Tuples -- Application -- Alternative to Dictionaries
"""

data_dict = dict(key1=100, key2=200, key3=300)
print(f'{data_dict=}')
print(f'{data_dict["key1"]=}')

from collections import namedtuple
Data = namedtuple('Data', data_dict.keys())
print(f'{Data._fields=}')
print(f'{data_dict.values()=}')

# Note: this doesn't work because the order of values is not guaranteed
data = Data(*data_dict.values())
print(f'{data=}')

# Instead, do this:
d2 = Data(**data_dict)
print(f'{d2=}')

"""
One application -- converting a list of dictionaries (e.g. retrieved from
a database) into a list of named tuples.
"""

data_list = [
    {'key2': 2, 'key1': 1},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)
print(f'{keys=}')

keys = {key for dict_ in data_list for key in dict_.keys()}
Struct = namedtuple('Struct', sorted(keys))
print(f'{Struct._fields=}')

"""
We must use default values
"""

Struct.__new__.__defaults__ = (None,) * len(Struct._fields)

example = Struct(key3=10)
print(f'{example=}')

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print(f'{tuple_list=}')
for tuple_ in tuple_list:
    print(f'{tuple_=}')

"""
Turning this generic process into a function
"""

def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

tuple_list = tuplify_dicts(data_list)
print(f'{tuple_list=}')
for tuple_ in tuple_list:
    print(f'{tuple_=}')