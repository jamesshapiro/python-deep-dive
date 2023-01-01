print('executing module1...')

value = 'module1 value'

# > python3
# >>> import module1
# $ executing module1...
# >>> module1.value
# $ 'module1 value'
# >>> module1.__file__
# $ '/[HOME]/code/python-deep-dive/007-modules-packages-and-namespaces/009-what-are-packages/packages-demo/module1.py''
# >>> module1.__package__
# $ ''
# >>> module1.__path__
# $ Traceback (most recent call last):
# $   File "<stdin>", line 1, in <module>
# $ AttributeError: module 'module1' has no attribute '__path__'
