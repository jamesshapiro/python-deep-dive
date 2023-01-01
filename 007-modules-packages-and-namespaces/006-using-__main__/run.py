# run.py

# print(f'loading run.py: __name__ = {__name__}')

# import module1

"""
Running:

> python3 run.py # yields:
$ loading run.py: __name__ = __main__
$ loading module1.py: __name__ = module1
"""

import timing

code = '[x**2 for x in range(1_000)]'
#code = '[x**2 for x in range(1_000_000)]'

result = timing.timeit(code, 100)
print(result)