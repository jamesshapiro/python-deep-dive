l = [1,5,4,10,9,6]

#print(f'{=}')
print(f'{sorted(l)=}')

l = ['c','B','D','a']
print(f'{sorted(l)=}')
print(f'{sorted(l,key=lambda item: item.lower())=}')

d = {'abc': 200, 'def': 300, 'ghi': 100}

print(f'{sorted(d, key=lambda x: d[x])}')

def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

print(f'{dist_sq(1+1j)=}')

l = [3+3j, 1-1j, 0, 3+0j]
try:
    sorted(l)
except TypeError as e:
    print(e)

print(f'{sorted(l, key=dist_sq)}')
print(f'{sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2)=}')

print('sorted gives you a stable-sort:')
l = ['Cleese','Idle','Palin','Chapman','Jones']
print(f'{sorted(l, key=lambda x: x[-1])=}')
l = ['Idle','Cleese','Palin','Chapman','Jones']
print(f'{sorted(l, key=lambda x: x[-1])=}')

print(f'{sorted(l, key=lambda x: x[::-1])=}')

import string
import random
# Challenge: Randomize an iterable using sorted
l = list(string.ascii_lowercase)
print(f'{sorted(l, key=lambda x: random.random())=}')
print(f'{sorted(l, key=lambda x: random.random())=}')