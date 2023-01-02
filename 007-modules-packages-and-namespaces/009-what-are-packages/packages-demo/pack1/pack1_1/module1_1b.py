# [FROM ../.. directory!]
# > python3
"""
>>> import pack1.pack1_1
'executing pack1...'
'executing pack1_1...'
>>> import sys
>>> 'pack1.pack1_1' in sys.modules
True
>>> 'pack1.pack1_1.module1_1b' in sys.modules
False
>>> 'pack1.pack1_1' in globals()
False
>>> 'pack1' in globals()
True
>>> pack1.pack1_1.__file__
/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/packages-demo/pack1/pack1_1/__init__.py'
>>> pack1.pack1_1.module1_1b.__file__
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: module 'pack1.pack1_1' has no attribute 'module1_1b'
>>> import pack1.pack1_1.module1_1b
'executing module1_1b...'
"""

"""
NOTE: importing pack1.pack1_1.module1_1b does NOT add anything to our globals!!!

>>> 'pack1.pack1_1.module1_1b' in globals()
False
>>> globals()
{
    '__name__': '__main__', 
    '__doc__': None, 
    '__package__': None, 
    '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    'pack1': <module 'pack1' from '/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/packages-demo/pack1/__init__.py'>, 
    'sys': <module 'sys' (built-in)>
}
"""

"""
>>> pack1.pack1_1.module1_1b.value
'module1_1b value'
>>> pack1.pack1_1.module1_1a.value
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: module 'pack1.pack1_1' has no attribute 'module1_1a'
>>> import pack1.pack1_1.module1_1a
'executing module1_1a...'
>>> pack1.pack1_1.module1_1a.value
'module1_1a value'
>>> globals()
{
    '__name__': '__main__', 
    '__doc__': None, 
    '__package__': None, 
    '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    'pack1': <module 'pack1' from '/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/packages-demo/pack1/__init__.py'>, 
    'sys': <module 'sys' (built-in)>
}
"""

"""
# HOWEVER!!!
>>> 'pack1.pack1_1.module1_1a' in sys.modules
True
>>> 'pack1.pack1_1.module1_1b' in sys.modules
True

# That is what has changed.
"""

"""
The takeaway is that just because you have loaded a package does not mean that
you have loaded any of the other modules in that package.

In order to access everything, we would need to write:
"""

"""
>>> import pack1.pack1_1.module1_1a
>>> import pack1.pack1_1.module1_1b
>>> import pack1.module1a
"""

"""
Sometimes as the author of a package, we don't want to require the user to
import everything. We want it to be the case that when the user types:

>>> import pack1.pack1_1

It automatically loads in module1_1a and module1_1b.

Remember that Package is a module, hence we can try to add the following to pack1/pack1_1/__init__.py:

import module1_1a
import module1_1b

But we get the following error:
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/packages-demo/pack1/pack1_1/__init__.py", line 5, in <module>
        import module1_1a
ModuleNotFoundError: No module named 'module1_1a'

This is because Python requires a path. Just because __init__.py is in the same directory as module1_1a.py does not mean that Python 
knows that it is in the same directory.

So there are two ways of doing it, but one of them is:

import pack1.pack1_1.module1_1a
import pack1.pack1_1.module1_1b
"""



print('executing module1_1b...')

value = 'module1_1b value'