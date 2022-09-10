# types are not binding by default
def func_1(a: int, b: int):
    return a * b

print('compiler ignoring type example:')
result = func_1('!', 20)
print(result)
print()

# This works because, by the time func_3()
# actually gets called, the program is
# able to know where to go to access the
# code for func_4 
def func_3():
    func_4()

def func_4():
    print('invoking a function that is not yet declared when the function is defined example:')

func_3()

# This fails (when uncommented). With
# NameError: name 'func_6' is not defined
# Because func_5 gets called and tries to 
# look up func_6 before func_6 is ever
# defined if all functions are declared at
# the top, that avoids this issue
# def func_5():
#     func_6()

# func_5()

# def func_6():
#     print('failed order example')

# prints: <class 'function'>
print()
print(f'{type(func_3)=}')
print()

other_func = func_3
print('other_func = func_3 # <- assigning a named function to a variable example:')
other_func()
print('print(other_func)')
print(f'{other_func=}')


print()
# Lambda functions
square = lambda x: x**2
print('square = lambda x: x**2 # <- assigning a lambda function to a variable example:')
print(square(5))

print()
print('print(square)')
print(f'{square=}')
print()

# prints: <class 'function'>
print(f'{type(square)=}')

# prints: <class 'function'>
print(f'{type(lambda x: x**2)=}')