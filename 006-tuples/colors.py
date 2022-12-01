from random import randint, random
from collections import namedtuple

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

Color = namedtuple('Color', 'red green blue alpha')
def named_tuple_random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)
