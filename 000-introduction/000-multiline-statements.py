extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_1 = True
extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_2 = True
extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_3 = True

# Demonstrating multiline functionality with "\"
# Note that no comments can follow the backslash
if extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_1 \
    and extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_2 \
    and extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_3:
    print('multiline if-statement success example\n')

# You cannot intersperse comments either. Uncomment to see what happens.
# if extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_1 \
#     # with interspersed comment
#     and extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_2 \
#     and extremely_long_variable_name_that_goes_on_and_on_ad_infinitum_3:
#     print('multiline if-statement with interspersed comment WILL FAIL with a syntax error')

"""
Multiline strings are not the same as comments. Unlike comments, they are
not ignore by the compiler. Rather they are compiled as part of your code.
In the non-multiline case, this is the same as declaring a string without
assigning it to a value 
"""

# This is equivalent to a multiline string, the compiler doesn't ignore it,
# but since it is not assigned, it's not doing anything
"non-assigned string"

multiline_example = """Multiline strings are not the same as comments. Unlike comments, they are
not ignore by the compiler. Rather they are compiled as part of your code.
In the non-multiline case, this is the same as declaring a string without
assigning it to a value 
"""

print(f"""multiline string variable example:
this variable and this print statement both illustrate the 
difference between multiline strings and comments:
{multiline_example=}'""")

# prints with newlines actually displayed as newlines
print('\nprettier print example:')
print(multiline_example)

# implicit line continuation examples
a = [
    1, #comments can be added here
    2 # or here
    , 3 # or here, but this is ugly
]

a = (
    1, # tuples are similar
    2
)

# syntactically valid, but not well-formatted
a = {
    'key1' # what about dicts?
    : 1    # this works too
    , 'key2' # even
    : # this
    2 # works
    , 'key3': 3
}

# same deal for function arguments
def my_func(a, # this is used to indicate...
            b, # another long comment here...
            c):
    print('multiline function args example')
    print(a,b,c)

my_func(
    10,
    20,
    30
)

a = 100
b = 100
c = 100

# example showing that you can indent arbitrarily for multi-line
if a > 10 \
    and b > 20 \
        and c > 30:
    print('\nmultiline if-statement whitespace example')
    print('all values are greater')