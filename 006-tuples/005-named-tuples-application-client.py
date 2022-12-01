from colors import random_color, named_tuple_random_color

"""
properties are completely opaque to the client
"""
color = random_color()
print(f'{color=}')

"""
properties are visible
"""
color = named_tuple_random_color()
print(f'{color=}')
print(f'{color.red=}')
print(f'{color.alpha=}')