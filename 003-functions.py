# types are not binding by default
def func_1(a: int, b: int):
    return a * b

result = func_1('=', 20)
print(result)


# This works because, by the time func_3()
# actually gets called, the program is
# able to know where to go to access the
# code for func_4 
def func_3():
    func_4()

def func_4():
    print('return order example')

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
print(type(func_3))
other_func = func_3
other_func()

# Lambda functions

square = lambda x: x**2
print(square(5))

# prints <function <lambda> at 0xfleventyfive>
print(square)

# prints: <class 'function'>
print(type(square))

# prints: <class 'function'>
print(type(lambda x: x**2))