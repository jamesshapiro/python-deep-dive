"""
Timing code using timeit

When we were looking at decorators we wrote a timing decorator. It could even
take a number of repititions as a parameter. This can be handy to time functions
directly in your code without affect the result of the function. But it wrote the 
results out to the console and sometimes we just want to access the timing data 
right inside our Python code.

The timeit module in Python is an alternative that works well for some things.
It is a little more complicated to use because it runs 'outside' our local namespace,
and you have to pass just small snippets of code to it (well you pass multi-line chunks
of code, but it gets tedious), and you also have to make it aware of your global or
local scope if that's needed by the code you want to time. One thing it does that we
did not do was temporarily disable the garbage collector. Still, there are lots of
pitfalls to benchmarking, and this approach, like ours, is good enough for most use
cases. YMMV.

It has the advantage that it can also be run directly from the command line.

Let's take a look at it
"""

from timeit import timeit

timeit(stmt='math.sqrt(2)', setup='import math', number=1_000_000)

timeit(stmt='sqrt(2)', setup='from math import sqrt', number=1_000_000)

import math
timeit(stmt='math.sqrt(2)', globals=globals(), number=1_000_000)

import random
l = random.choices(list('python'), k=500)
'l' in globals()
'm' in globals()

timeit(stmt='random.choice(l)', globals=globals())

def pick_random():
    randoms = random.choices(list('python'), k=500)
    print('randoms' in locals())
    timeit(stmt='random.choice(randoms)',
           setup='import random',
           globals=locals())

'randoms' in globals()
pick_random()

def pick_random(lst):
    return random.choice(lst)

timeit(stmt='pick_random(l)', globals=globals())