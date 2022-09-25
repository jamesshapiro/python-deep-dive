import time

def time_it(fn, *args, **kwargs):
    print(f'{args=},{kwargs=}')

time_it(print, 1, 2, 3, sep=' - ', end=' *** ')

def time_it(fn, *args, **kwargs):
    fn(args,kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' *** ')
print((1,2,3), {'sep':' - ','end': ' *** '})

def time_it(fn, *args, **kwargs):
    fn(*args,**kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' *** ')

print('\n')

def time_it(fn, *args, rep=1, **kwargs):
    for _ in range(rep):
        fn(*args,**kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for _ in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()
    avg_time = (end - start) / rep
    print(avg_time)
    return avg_time

time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)

def compute_powers_1(n, *, start=1, end):
    # using a for-loop
    results = []
    for i in range(start,end):
        results.append(n**i)
    return results

compute_powers_1(2, end=5)

def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    results = [n**i for i in range(start,end)]
    return results

compute_powers_2(2, end=5)

def compute_powers_3(n, *, start=1, end):
    # using generators expression
    results = (n**i for i in range(start,end))
    return results

list(compute_powers_3(2, end=5))

time_it(compute_powers_1, 2, start=0, end=20000, rep=5)
print('\nNote: here n is getting passed in via kwargs')
time_it(compute_powers_2, n=2, start=0, end=20000, rep=5)
time_it(compute_powers_3, 2, start=0, end=20000, rep=5)

def compute_powers_3(n, *, start=1, end):
    # using generators expression
    results = list(n**i for i in range(start,end))
    return results

time_it(compute_powers_3, 2, start=0, end=20000, rep=5)