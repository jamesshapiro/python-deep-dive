"""
Reloading Modules
"""
import os
import sys

def create_module_file(module_name, **kwargs):
    '''
    Create a module file named <module_name>.py
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs
    '''
    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.join(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint(f'{key} = {value}')\n")

create_module_file('test', k1=10, k2='python')

import test
test.print_values()

create_module_file('test', k1=20, k2='python', k3='grail')
import test
test.print_values()
"""
Note: Python does not reload the module
because the module name is already cached in sys.modules
"""

# One hacky solution:
del sys.modules['test']

import test
test.print_values()

"""
But this doesn't quite work, because it only changes the reference
in the current module, not in the namespace of all other modules
"""

print(f'{hex(id(test))=}')
print(f'{hex(id(sys.modules["test"]))=}')

create_module_file('test', k1=10, k2='python', k3='grail', k4='parrots')

import importlib
importlib.reload(test)

# This overwrites the section of memory referred to by the old address
# to point to the new module. Hence, even if this code is loaded in
# another module, the new module will be used
print(f'{hex(id(test))=}')
print(f'{hex(id(sys.modules["test"]))=}')

# This can be done when you are developing, but should not be done
# in production code

create_module_file('test2', k1='python')

from test2 import print_values
print_values()
print(f"{'test2' in globals()}")
print(f"{'test2' in sys.modules}")

create_module_file('test2', k1='python', k2='monty')
importlib.reload(sys.modules['test2'])
print_values()

"""
NOTE: print_values is still bound to the old module!!!

Would need to re-import the function to get it to work
"""
from test2 import print_values

"""
Or, alternatively:
"""
print_values = sys.modules['test2'].print_values

"""
And again, after the reload, anyone who loaded something from the module
that is not the module itself will need to re-import it. Hence why you
can reload but it is not going to be safe and will probably break things
"""