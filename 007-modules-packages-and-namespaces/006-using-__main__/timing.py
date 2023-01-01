# timing.py # invoke with  python3 timing.py "[x**2 for x in range(100_000)]" -r 15
"""
Times how long a snippet of code takes to run over multiple iterations.
"""
print('loading timing...')

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'repeats elapsed average')

def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)

# goal with argparse is to be able to run this script from the command line
# e.g.:
# > python3 timing.py "code..." -r 100
# However, I only want this to run if I am invoking this script directly

if __name__ == '__main__':
    # get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'code',
        type=str,
        help='The Python code snippet to time.'
    )
    parser.add_argument(
        '-r', '--repeats',
        type=int,
        default=10,
        help='The number of times to repeat the test.'
    )
    args = parser.parse_args()
    #print(f'{args.code=}')
    #print(f'{args.repeat=}')
    print(f'timing: {args.code}...')
    print(timeit(code=str(args.code), repeats=args.repeats))
    # python3 timing.py "[x**2 for x in range(100_000)]" -r 15

"""
Note: some built-in modules already work like this (offering the ability to
invoke them from the command line). E.g.:

> python3 -m zipfile -c app.zip module1.py run.py timing.py
> python3 -m zipfile -l app.zip
"""
