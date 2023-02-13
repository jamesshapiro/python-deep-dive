#import sys

# example 1
#print(f'{sys.argv=}')

# example 3
#numbers = [int(number) for number in sys.argv[1:]]
#print(f'{sum(numbers)=}')

# example 4
# --last-name Cleese --first-name John

# example 5
# python3 command_line_arguments.py 10 3

# import argparse
# parser = argparse.ArgumentParser(description='Calculates the div and mod of two numbers: a and b')
# parser.add_argument('a', type=int, help='first integer')
# parser.add_argument('b', type=int, help='second integer')

# args = parser.parse_args(['100','300'])

# print(args.a)
# print(args.b)

# args = parser.parse_args(sys.argv[1:])
# print(args.a)
# print(args.b)

# a = args.a
# b = args.b

# print(f'{a}//{b} = {a//b}, {a}%{b} = {a%b}')

# example 6
# python3 command_line_arguments.py  -f Polly -l Parrot --yob 1969

# import argparse
# import datetime

# parser = argparse.ArgumentParser(description='Returns a string containing the name and age of the person')

# parser.add_argument('-f', '--first', help='first name', type=str, required=False, dest='first_name')
# parser.add_argument('-l', '--last', help='last name', type=str, required=True, dest='last_name')
# parser.add_argument('--yob', help='year of birth', type=int, required=True, dest='birth_year')

# args = parser.parse_args()

# names = []
# if args.first_name:
#     names.append(args.first_name)
# names.append(args.last_name)
# full_name = ' '.join(names)

# current_year = datetime.datetime.utcnow().year
# age = current_year - args.birth_year

# print(f'{full_name} is {age} years old')

#example 7
# import argparse

# parser = argparse.ArgumentParser(description='Prints the squares of a list of numbers, and the cubes of another list of numbers')

# parser.add_argument('--sq', type=float, nargs='*', help='list of numbers to square')
# parser.add_argument('--cu', type=float, nargs='+', help='list of numbers to cube')

# args = parser.parse_args()

# # i.e. if args.sq is not None and len(args.sq) > 0:
# # python3 command_line_arguments.py --cu 1 2 3 4
# if args.sq:
#     print(f'{args.sq=}')
#     squares = [number**2 for number in args.sq]
#     print(f'{[number**2 for number in args.sq]=}')

# cubes = [number**3 for number in args.cu]
# print(f'{[number**3 for number in args.cu]=}')

# example 8
# python3 command_line_arguments.py --monty Sage
# python3 command_line_arguments.py --monty
# python3 command_line_arguments.py --monty --n Eric
# python3 command_line_arguments.py -v

#import argparse

#parser = argparse.ArgumentParser(description='testing defaults and flags')

# parser.add_argument('--monty', action='store_const', const='Python')
# parser.add_argument('--n', '--name', default='John')

# implementing flags, example #1:
#parser.add_argument('-v', '--verbose', action='store_const', const=True, default=False)

# implementing flags (another method)
# parser.add_argument('-v2', action='store_const', const=True)

# best way to write flags
#parser.add_argument('-q', '--quiet', action='store_true')

# FINALLY, mutually exclusive options, e.g. --verbose and --quiet cannot be used together
#args = parser.parse_args()
#print(args)

# example 9
# python3 command_line_arguments.py -n 10

import argparse
import cmath

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true')
group.add_argument('-q', '--quiet', action='store_true')
parser.add_argument('-n', type=complex, required=True)

args = parser.parse_args()
print(args)

if args.quiet:
    print('quiet mode...')
    print('nothing to see here, move along')
elif args.verbose:
    print('verbose mode...')
    print(f'input: {args.n}')
    print(f'real part: {args.n.real}')
    print(f'imaginary part: {args.n.imag}')
    print(f'{args.n} = {cmath.polar(args.n)}')
else:
    print('normal mode...')
    print(f'{args.n} = {cmath.polar(args.n)}')