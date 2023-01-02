# [FROM ../.. directory!]
# > python3
"""
>>> import module1_1a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'module1_1a'
>>> import pack1.pack1_1.module1_1a
executing pack1...
executing pack1_1...
executing module1_1a...
>>> import sys
>>> 'pack1' in sys.modules
True
>>> 'pack1.pack1_1' in sys.modules
True
>>> 'pack1.pack1_1.module1_1a' in sys.modules
True
>>> 'pack1' in globals()
True
>>> 'pack1.pack1_1' in globals()
False
>>> 'pack1.pack1_1.module1_1a' in globals()
False


"""

print('executing module1_1a...')

value = 'module1_1a value'