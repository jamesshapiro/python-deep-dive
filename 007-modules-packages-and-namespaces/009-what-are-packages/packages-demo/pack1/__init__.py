# [FROM .. directory!]
# > python3
# >>> import pack1
# $ 'executing pack1...'
# >>> pack1.value
# $ 'pack1 value'
# >>> type(pack1)
# $ <class 'module'>
# >>> import module1
# $ 'executing module1...'
# >>> type(module1)
# $ <class 'module'>
# >>> pack1.__file__
# $ '/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/app/pack1/__init__.py'
# >>> pack1.__package__
# $ 'pack1'
# >>> pack1.__path__
# $ ['/Users/brad/Code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/app/pack1']

print('executing pack1...')
value = 'pack1 value'
