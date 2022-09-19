# We want to avoid the approximation issues with binary floats

# Why not just use Fractions?

# But if there are finite number of significant digits, then
# any number can be expressed as a rational number, so why
# not just use the Fraction class?

# Fraction class involves many computations, even for something
# simple like addition (partly because you have to simplify the)
# result after adding. Complex. Also requires more memory

# Why not just use floats?

# In finance, banking, and other fields, exact finite representations
# are highly desirable

# Decimals have a context that controls certain aspects of working
# with decimals

# - precision during arithmetic operations
# - rounding algorithm

# This context can be global -> the default context
# or it can be temporary (local)

import decimal
from decimal import Decimal

print('Default context:')
print(f'{decimal.getcontext()=}') # default context
print(f'{decimal.getcontext().prec=}')
#decimal.localcontext(ctx=None) # local context
decimal.getcontext().prec=6
print('The default context can be modified')
print(f'{decimal.getcontext()=}') # default context
print(f'{decimal.getcontext().prec=}\n')

g_ctx = decimal.getcontext()
print("Note: ROUND_HALF_EVEN is Banker's rounding, same as for the default round() function")
print(f'{g_ctx.rounding=}')
print("Note: ROUND_HALF_UP is how we intuitively round to infinity (I think)")
print('g_ctx.rounding = decimal.ROUND_HALF_DOWN')
g_ctx.rounding = decimal.ROUND_HALF_DOWN
print(f'{g_ctx=}') # default context
print(f'{g_ctx.prec=}')
print(f'{g_ctx.rounding=}\n')

note = """
decimal.getcontext() returns the default context, but decimal.localcontext() 
returns a context manager:"""
print(note)
l_ctx = decimal.localcontext()
print(f'{type(decimal.getcontext())=}')
print(f'{type(decimal.localcontext())=}')

x_1 = Decimal('0.5')
x_2 = Decimal('1.5')
x_3 = Decimal('2.5')
x_4 = Decimal('3.5')
y_1 = Decimal('-0.5')
y_2 = Decimal('-1.5')
y_3 = Decimal('-2.5')
y_4 = Decimal('-3.5')

print('\nWorking with Local Contexts:')
with decimal.localcontext() as ctx:
    print(f'{type(ctx)=}')
    ctx.prec = 2
    ctx.rounding = decimal.ROUND_HALF_UP
    print('decimal.getcontext() grabs the context which, inside this current context manager, is the local context')
    print(decimal.getcontext())
    print('\nROUND HALF UP IN LOCAL CONTEXT')
    print(f'{round(x_1,0)=}')
    print(f'{round(x_2,0)=}')
    print(f'{round(x_3,0)=}')
    print(f'{round(x_4,0)=}')
    print(f'{round(y_1,0)=}')
    print(f'{round(y_2,0)=}')
    print(f'{round(y_3,0)=}')
    print(f'{round(y_4,0)=}')

print('\nROUND HALF DOWN IN GLOBAL CONTEXT')
print(f'{round(x_1,0)=}')
print(f'{round(x_2,0)=}')
print(f'{round(x_3,0)=}')
print(f'{round(x_4,0)=}')
print(f'{round(y_1,0)=}')
print(f'{round(y_2,0)=}')
print(f'{round(y_3,0)=}')
print(f'{round(y_4,0)=}')
decimal.getcontext().rounding = decimal.ROUND_HALF_UP