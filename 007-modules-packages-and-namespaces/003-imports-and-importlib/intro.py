"""
Imports and importlib
"""
import sys
import os
import collections

mod_name = 'math'

try:
    import mod_name
except ModuleNotFoundError as e:
    print(e)

import importlib
importlib.import_module(mod_name)

try:
    print(f'{math.sqrt(2)=}')
except NameError as e:
    print(e)

print(f'{"math" in sys.modules=}')
print(f'{"math" in globals()=}')

math = sys.modules['math']
print(f'{math.sqrt(2)=}')

"""
- finders
- loaders
- finder + loader == importer

The finder returns a module spec, e.g. The spec contains:
- name
- loader
- origin
"""
fractions = importlib.import_module('fractions')
print(f'{fractions.__spec__=}')

"""
The finder objects are in sys.meta_path
"""
print(f'\n{sys.meta_path=}')

""" Can get the spec using """
print(f'\n{importlib.util.find_spec("decimal")=}')
print(f'\n{importlib.util.find_spec("module1")=}')

import module1
print(f'{"module1" in globals()=}')
print(f'{module1.a=}')

ext_module_path = os.environ['HOME'] + '/temp-external'
print(f'{ext_module_path=}')
file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as f:
    f.write("print('running module2.py...')\n")
    f.write("x = 'python'\n")

print(f"\n{importlib.util.find_spec('module2')=}")
print(f'\n{sys.path=}')
sys.path.append(ext_module_path)

print(f"\n{importlib.util.find_spec('module2')=}")

import module2

print(f'{module2.x=}')