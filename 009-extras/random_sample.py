import random

result = random.choices(list('abc'), k=10)
print(result)

l = list(range(10))
print(l)

print('\nThis runs the risk of having repetitions')
print(f'{random.choices(l, k=5)=}\n')

print('\nTo get a sample without repetitions, use sample()')
print(f'{random.sample(l, k=5)=}\n')

try:
    print(f'{random.sample(l, k=11)=}\n')
except ValueError as e:
    print(f'{e=}')

suits = 'C', 'D', 'H', 'S'
ranks = tuple(range(2, 11)) + tuple('JQKA')

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(str(rank) + suit)

#print(deck)

# more simply:
from collections import Counter

deck = [str(rank) + suit for suit in suits for rank in ranks]

print(Counter(random.choices(deck, k=40)))

print(Counter(random.sample(deck, k=40)))