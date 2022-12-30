"""
In this example, we look at a simplified view of how Python imports a module

We use two built-in functions, compile and exec.

The compile function compiles source (e.g. text) into a code object.

The exec function is used to execute a code object.

In our case we are going to want to use our module's __dict__.
"""

# main.py
import os.path
import types
import sys

# let's "import" module1 manually

# first we need to load the code from file

# Note: the module name does not have to match the file name, even though that is the default
module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# next we create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# insert a reference to the module in sys.modules
sys.modules[module_name] = mod

# compile the module source code into a code object
# optionally we should tell the code object where the source came from
# the third parameter is used to indicate that our source consists of a sequence of statements
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# execute the module
# we want the global variables to be stored in mod.__dict__
exec(code, mod.__dict__)

# our module is now imported!
# We can use it directly via our mod variable

mod.hello()

# but we can also import it, using the module name we specified
# note that this is retrieved from the sys.modules path.
# if you commented out the code above, it would throw an error
# saying that the module was not found.
import module1

module1.hello()




