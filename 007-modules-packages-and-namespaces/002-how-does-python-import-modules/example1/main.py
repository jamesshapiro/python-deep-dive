# main.py

print('================================')
print(f'Running main.py - module name: {__name__}')

import module1
print('importing module 1 again...')
# Note: it does not actually import it again because it is cached
import module1

print(f'{module1=}')

module1.pprint_dict('main.globals', globals())

import sys
print(f'{sys.path=}')
print(f'{sys.modules=}')

print('================================')