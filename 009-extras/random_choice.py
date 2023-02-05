import random
from collections import Counter

l = list(range(1,1001))
print(random.choice(l))
print(random.choices(l, k=10))

l = ['a', 'b', 'c']
weights = [10, 1, 1]

print(random.choices(l, weights=weights, k=10))

random.seed(0)

counter = Counter([random.randint(0, 10) for _ in range(1_000_000)])
print(counter)

cumulative_weights = [7,8,10]

print(random.choices(l, cum_weights=cumulative_weights, k=10))