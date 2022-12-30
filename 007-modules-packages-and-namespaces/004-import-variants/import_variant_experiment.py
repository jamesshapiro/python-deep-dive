import sys

#print(f'{sys.modules["math"]}')
try:
    print(f'{sys.modules["math"]}')
except KeyError as e:
    print(f'Key Error: {e} not found in sys.modules')

from math import sqrt
print(f'{sys.modules["math"]}')