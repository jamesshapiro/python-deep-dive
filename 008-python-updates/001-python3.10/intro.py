# Relevant Python Changes 3.10

# Structural Pattern Matching
def respond(language):
    match language:
        case "Java":
            return "Hmm, coffee!"
        case "Python":
            return "I'm not scared of snakes!"
        case "Rust":
            return "Don't drink too much water!"
        case "Go":
            return "Collect $200"
        case _:
            return "I'm sorry"

print(f'{respond("Python")=}')
print(f'{respond("Go")=}')
print(f'{respond("Fortran")=}')

# But we can do even more!

def respond(language):
    match language:
        case "Java" | "Javascript":
            return "Hmm, coffee!"
        case "Python":
            return "I'm not scared of snakes!"
        case _:
            return "I'm sorry"

print('='*40)
print(f'{respond("Java")=}')
print(f'{respond("Javascript")=}')
print(f'{respond("Fortran")=}')

#######################
symbols = {
    'F': '\u2192',
    'B': '\u2190',
    'L': '\u2191',
    'R': '\u2193',
    'pick': '\u2923',
    'drop': '\u2925'
}
#######################

def op(command):
    match command:
        case "move F":
            return symbols['F']
        case "move B":
            return symbols['B']
        case "move L":
            return symbols['L']
        case "move R":
            return symbols['R']
        case "pick":
            return symbols['pick']
        case "drop":
            return symbols['drop']
        case _:
            raise ValueError(f"{command} does not compute!")

op("move L")
print([
    op("move F"),
    op("move F"),
    op("move L"),
    op("pick"),
    op("move R"),
    op("move L"),
    op("move F"),
    op("drop"),
])

def op(command):
    match command:
        case ["move", ("F" | "B" | "L" | "R") as direction]:
            return symbols[direction]
        case "pick":
            return symbols['pick']
        case "drop":
            return symbols['drop']
        case _:
            raise ValueError(f"{command} does not compute!")

print([
    op(["move", "F"]),
    op(["move", "F"]),
    op(["move", "L"]),
    op("pick"),
    op(["move", "R"]),
    op(["move", "L"]),
    op(["move", "F"]),
    op("drop"),
])

def op(command):
    match command:
        case ["move", *directions]:
            return tuple(symbols[direction] for direction in directions)
        case "pick":
            return symbols['pick']
        case "drop":
            return symbols['drop']
        case _:
            raise ValueError(f"{command} does not compute!")

print([
    op(["move", "F", "F", "L"]),
    op("pick"),
    op(["move", "R", "L", "F"]),
    op("drop"),
])


def op(command):
    match command:
        case ["move", *directions] if set(directions) <= symbols.keys():
            return tuple(symbols[direction] for direction in directions)
        case "pick":
            return symbols['pick']
        case "drop":
            return symbols['drop']
        case _:
            raise ValueError(f"{command} does not compute!")

try:
    print(op(["move", "UP"]))
except ValueError as e:
    print(e)

# Additional reading PEP 636: https://peps.python.org/pep-0636/

#============ Zip Options ============

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4]

print(list(zip(l1, l2)))
from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='???')))

try:
    print(list(zip(l1, l2, strict=True)))
except ValueError as e:
    print(e)