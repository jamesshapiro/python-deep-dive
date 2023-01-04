import common.validators

common.validators.boolean.is_boolean('True')

"""
So that's great, but we still have this .boolean.

What if we just want to bundle them all up under common.validators?

See: package_imports_better_yet/
"""

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)

print('\n\n***** numeric *****')
for k in common.validators.numeric.__dict__.keys():
    print(k)
