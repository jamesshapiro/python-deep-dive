import shared.validators as validators
import shared

#common.validators.boolean.is_boolean('True')

"""
So that's great, but we still have this .boolean.

What if we just want to bundle them all up under common.validators?

Use *!!!
"""

validators.is_boolean('True')
validators.is_json('{}')

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')
for k in shared.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in validators.__dict__.keys():
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
for k in validators.numeric.__dict__.keys():
    print(k)

"""
We solved both of the problems!

First, we used relative imports.

Second we used _ to prefix the names of the non-numeric helper functions to
keep them out of the validator namespace.

Third, as an alternative in the numeric module, we used:

__all__ = ['is_integer', 'is_numeric']

To exclude the helper functions from the validators namespace.
"""
