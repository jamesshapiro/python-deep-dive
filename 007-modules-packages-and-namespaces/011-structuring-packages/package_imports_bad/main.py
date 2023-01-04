import common.validators.boolean
import common.validators.date
import common.validators.json
import common.validators.numeric

common.validators.json.is_json('{}')
common.validators.date.is_date('2023-01-01')

# this will run just fine, but it's not user-friendly



"""
print('\n\n***** self *****')
for k in globals().keys():
    print(k)

This yields the following error:
Traceback (most recent call last):
  File "main.py", line 14, in <module>
     for k in globals().keys():
RuntimeError: dictionary changed size during iteration

Because 'k' itself is a global in global.keys()

So instead we do the following:
"""
print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

"""
This prints:

***** self *****
__name__
__doc__
__package__
__loader__
__spec__
__annotations__
__builtins__
__file__
__cached__
common

Note that common is the only 3rd party package
"""

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

"""
This prints:

***** common *****
__name__
__doc__
__package__
__loader__
__spec__
__path__
__file__
__cached__
__builtins__
validators
"""

print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)

"""
This prints:

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
date
json
isnumeric

"""

print('\n\n***** numeric *****')
for k in common.validators.numeric.__dict__.keys():
    print(k)

"""
This prints:

***** numeric *****
__name__
__doc__
__package__
__loader__
__spec__
__file__
__cached__
__builtins__
is_integer
is_numeric
numeric_helper_1
numeric_helper_2
"""

"""
This works, but it's not user-friendly and is very tedious
for the user to type out

Could do something like:

from common.validators.numeric import is_integer, is_numeric
is_integer(1)
is_numeric(10)

But this is arguably even more tedious
"""

"""
Would be better to have something like:

import common.validators as validators

validators.is_numeric(20)
validators.is_integer('200')

But this won't work out of the box. Would need to do something like:
validators.numeric.is_integer('200')

Which is still tedious. There must be a better way
"""