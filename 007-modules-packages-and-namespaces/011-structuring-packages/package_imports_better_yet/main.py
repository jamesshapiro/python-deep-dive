import common.validators

#common.validators.boolean.is_boolean('True')

"""
So that's great, but we still have this .boolean.

What if we just want to bundle them all up under common.validators?

Use *!!!
"""

common.validators.is_boolean('True')
common.validators.is_json('{}')

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)

"""
Note that here we have:

***** validators *****
__name__
__doc__
__package__
__loader__
__spec__
__path__
__file__
__cached__
__builtins__
boolean
is_boolean
boolean_helper_1
boolean_helper_2
date
is_date
date_helper_1
date_helper_2
json
is_json
json_helper_1
json_helper_2
numeric
is_integer
is_numeric
numeric_helper_1
numeric_helper_2

"""

print('\n\n***** numeric *****')
for k in common.validators.numeric.__dict__.keys():
    print(k)

"""
HOWEVER, the downside to this is that it contains all of the functions
including the private helper functions.
"""

"""
A second issue, suppose that at some point we decide to rename the
package from "common" to "shared". We would have to change all of the
imports in all of the files. This is a maintenance nightmare.

Solution: Use relative imports!

See: package_imports_better_yet_2/
"""