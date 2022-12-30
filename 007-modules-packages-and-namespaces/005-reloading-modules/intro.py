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

