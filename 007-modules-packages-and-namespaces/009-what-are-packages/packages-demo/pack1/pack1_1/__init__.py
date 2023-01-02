# [FROM ../.. directory!]
# > python3
"""
>>> import pack1_1
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pack1_1'

>>> import pack1.pack1_1
'executing pack1...'
'executing pack1_1...'
>>> pack1.pack1_1.value
'pack1_1 value'
>>> type(pack1.pack1_1)
<class 'module'>
>>> pack1.pack1_1.__file__
'/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/app/pack1/pack1_1/__init__.py'
>>> pack1.pack1_1.__package__
'pack1.pack1_1'
>>> pack1.pack1_1.__path__
'/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/app/pack1/pack1_1'
>>> pack1_1.value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pack1_1' is not defined
>>> 'pack1_1' in globals()
False
>>> import sys
>>> 'pack1_1' in sys.modules
False
>>> 'pack1.pack1_1' in sys.modules
True
>>> 'pack1.pack1_1' in globals()
False
>>> 'pack1' in globals()
True
>>> from pack1 import pack1_1
>>> id(pack1_1) == id(sys.modules['pack1.pack1_1'])
True
"""


"""
What's going on here?
"""


print('executing pack1_1...')
value = 'pack1_1 value'
