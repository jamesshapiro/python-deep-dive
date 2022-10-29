"""
Free Variables and Closures

Remember: Functions defined inside another function can access the
outer (nonlocal) variables
"""

def outer():
    x = 'python'

    # This x refers to the one in outer's scope
    # this nonlocal variable x is called a *free* variable
    #
    # When we consider inner, we really are looking at:
    #    - the function inner
    #    - the free variable x (with current value python)
    #
    # This is called a *closure*
    def inner():
        print(f'{x} rocks!')
    
    inner()

#outer()

"""
Returning the inner function

What happens if, instead of calling (running) inner from
inside outer, we return it?
"""

def outer():
    x = 'python'
    # x is a free variable in inner
    # it is bound to the variable x in outer
    # and this happens when outer runs (i.e. when inner is created)
    # this is the closure
    def inner():
        print(f'{x} rocks!')
    return inner

# We can assign that return value to a variable name

fn = outer()
fn()

"""
When we called fn, at that time Python determined the value of x
in the extended scope.

BUT notice that outer had finished running before we called fn.
Its scope was "gone"
"""

"""
Python Cells and Multi-Scoped Variables

Here the value of x is *shared* between two scopes:
    - outer
    - closure
The label x is *in two different scopes*, but always references the same value

Python does this by creating a *cell* as an intermediary object

                    +-------------------------+       +-------------------------+
outer.x ----|       | cell             0xA500 |       | str              0xFF10 |       
            |       |                         |       |                         |       
            |-----> |          0xFF100  ----- | ----> |           "python"      |
            |       |                         |       |                         |       
inner.x ----|       |                         |       |                         |       
                    +-------------------------+       +-------------------------+       

Key:
    "0xA500" memory address of the cell itself
    "0xFF100" reference to another object

In effect, both variables x (in outer and inner), point to the same *cell*

When requesting the value of the variable, Python will "double-hop"
to get to the final value

"""
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

"""
Closures

You can think of the closure as:
    - a function, plus
    - an extended scope that contains the *free variables*

The free variable's value is the object the cell points
to -- so that could change over time.

Every time the function in the closure is called
and the free variable is referenced:

Python looks up the *cell* object, and then whatever the cell
is pointing to
"""
def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10 # local variable
        print(f'{x} rocks!')
    return inner

fn = outer() # fn -> inner + extended scope (x)

"""
Introspection
"""
def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10 # local variable
        print(f'{x} rocks!')
    return inner

fn = outer()
# tuple with all of the free variable labels
print(f'{fn.__code__.co_freevars=}')
# tuple with all of the cells
print(f'{fn.__closure__=}')

# also does the double hop to look up the object id
# of the object referred to by the cell.
def outer():
    x = 'python'
    print(f'{hex(id(x))=}')
    def inner():
        print(f'{hex(id(x))=}')
        a = 10 # local variable
        print(f'{x} rocks!')
    return inner

print()
fn = outer()
fn()
print(f'{fn.__code__.co_freevars=}')
print(f'{fn.__closure__=}')

"""
Modifying free variables
"""
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

counter_1 = counter()
print(f'{counter_1()=}')

"""
Multiple Instances of Closures

Every time we run a function, a new scope is created.

If that function generates a closure a new closure is created every time as well
"""
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

counter_1 = counter()
counter_2 = counter()

print()
print(f'{counter_1()=}')
print(f'{counter_1()=}')
print(f'{counter_1()=}')
print(f'{counter_2()=}')
print(f'{counter_2()=}')
print(f'{counter_2()=}')
print('\nNote: Different memory addresses for different cells')
print(f'{counter_1.__closure__=}')
print(f'{counter_2.__closure__=}')

"""
counter_1 and counter_2 do not have the same extended scope. They are
different instances of the closure.

The cells are different
"""

"""
Share Extended Scopes
- count (inc1) is a free variable -- bound to count in the extended scope
- count (inc2) is a free variable -- bound to the same *count*
"""
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2

print()
counter_1, counter_2 = outer()
print(f'{counter_1()=}')
print(f'{counter_1()=}')
print(f'{counter_1()=}')
print(f'{counter_2()=}')
print(f'{counter_2()=}')
print(f'{counter_2()=}')
print('\nNote: Same memory addresses because same cell')
print(f'{counter_1.__closure__=}')
print(f'{counter_2.__closure__=}')

"""
Shared Extended Scopes

You may think this shared extended scope is highly unusual... but it's not!

It happens often by mistake. The following is NOT an example
"""
def adder(n):
    def inner(x):
        return x + n
    return inner

"""
Three different closures -- no shared scopes, so far so good
"""
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

add_1(0)

print(f'{add_1(0)=}')
print(f'{add_2(0)=}')
print(f'{add_3(0)=}')

"""
Shared Extended Scopes

But suppose we tried doing it this way:

- n = 1: the free variable in the lambda is n, and it is bound to the n we created in the loop
- n = 2: the free variable in the lambda is n, and it is bound to the (same) n we created in the loop
- n = 3: the free variable in the lambda is n, and it is bound to the (same) n we created in the loop

Now we could call the adders in the following way:
"""
adders = []
for n in range(1,4):
    adders.append(lambda x: x + n)

print(f'{adders[0](10)=}')
print(f'{adders[1](10)=}')
print(f'{adders[2](10)=}')
"""
Remember, Python does not "evaluate" the free variable n until adders[i] is called

Since all three functions in adders are bound to the same n, by the time we call adders[0],
the value of n is 3 (the last iteration of the loop set n to 3)
"""
print()
adders = []
for idx, n in enumerate(range(1,4)):
    adders.append(lambda x: x + n)
    print(f'{adders[idx](10)=}')
print(f'{adders[0](10)=}')
print(f'{adders[1](10)=}')
print(f'{adders[2](10)=}')

"""
Nested Closures
"""
def incrementer(n):
    # inner + n is a closure
    def inner(start):
        current = start
        # inc + current + n is a closure
        def inc():
            nonlocal current
            current += n
            return current
        
        return inc
    return inner

inc_1 = incrementer(10)(0)

print()

print(f'{inc_1()=}')
print(f'{inc_1()=}')
print(f'{inc_1()=}')

fn = incrementer(2)
print()
print(f'{fn.__code__.co_freevars=}')
zero_starter = fn(0)
print(f'{zero_starter()=}')
print(f'{zero_starter()=}')
print(f'{zero_starter()=}')
print(f'{zero_starter.__code__.co_freevars=}')
hundred_starter = fn(100)
print(f'{hundred_starter()=}')
print(f'{hundred_starter()=}')
print(f'{hundred_starter()=}')
print(f'{hundred_starter.__code__.co_freevars=}')

########## CODING SECTION #########

def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

fn = outer()
print(f'\n{fn.__code__.co_freevars=}')
print(f'{fn.__closure__=}')

def outer():
    x = 'python'
    y = 'hello world'
    def inner():
        print(x, y)
    return inner

fn = outer()
print(f'\n{fn.__code__.co_freevars=}')
print(f'{fn.__closure__=}')

"""
Confusing behavior that doesn't line up with the lecture, possibly
due to interning / compile-time optimizations
"""
def outer():
    x = [1,2,3]
    print(f'outer x address: {hex(id(x))=}')
    def inner():
        x = [1,2,3]
        x.append(4)
        print(f'{x=}')
        print(f'inner x address: {hex(id(x))=}')
    print(f'{x=}')
    return inner

print()
fn_1 = outer()
#fn_2 = outer()
fn_1()
print(f'{fn_1.__code__.co_freevars=}')
print(f'{fn_1.__closure__=}')
#print(f'{fn_2.__code__.co_freevars=}')
#print(f'{fn_2.__closure__=}')

"""
Another attempt
"""
def outer():
    x = [1,2,3]
    print(f'outer x address: {hex(id(x))=}')
    def inner():
        y = x
        y.append(4)
        print(f'{y=}')
        print(f'inner y=x address: {hex(id(y))=}')
    print(f'{x=}')
    return inner

print()
fn_1 = outer()
fn_1()
print(f'{fn_1.__code__.co_freevars=}')
print(f'{fn_1.__closure__=}')

"""
Modifying free variable
"""
def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        print(f'{hex(id(count))=}')
        print(count)
        return count
    return inc

fn = outer()
print()
print(f'{fn.__code__.co_freevars=}')
print(f'{fn.__closure__=}')
print(f'{hex(id(0))=}')
fn()
fn()

"""
"""
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        print(count)
        return count
    
    def inc2():
        nonlocal count
        count += 1
        print(count)
        return count
    
    return inc1, inc2

fn1, fn2 = outer()
print()
print(f'{fn1.__code__.co_freevars=}')
print(f'{fn1.__closure__=}')
print(f'{fn2.__code__.co_freevars=}')
print(f'{fn2.__closure__=}')
fn1()
fn2()
fn1()

"""
Another closure example, this one unique to the coding section

"""
def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
print()
print(f'{square.__closure__=}')
print(f'{hex(id(2))=}')
print(f'{square=}')
print(f'{square(5)=}')

cube = pow(3)
print(f'{cube.__closure__=}')
print(f'{hex(id(3))=}')
print(f'{cube=}')
print(f'{cube(5)=}')

"""
Shared Extended Scopes

Non-example
"""
def adder(n):
    def inner(x):
        return x + n
    return inner

"""
Three different closures -- no shared scopes, so far so good
"""
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
print()
# Note: different closures
print(f'{add_1.__closure__=}')
print(f'{add_2.__closure__=}')
print(f'{add_3.__closure__=}')
print(f'{add_1(0)=}')
print(f'{add_2(0)=}')
print(f'{add_3(0)=}')

"""
Three different closures -- shared scope, disaster
"""
adders = []
for n in range(1,4):
    adders.append(lambda x: x + n)
print()
print(f'{adders[0](10)=}')
print(f'{adders[1](10)=}')
print(f'{adders[2](10)=}')
# These are technically not closures, so this is what we would expect to see
print(f'{adders[0].__closure__=}')
print(f'{adders[1].__closure__=}')
print(f'{adders[2].__closure__=}')

"""
Adders example continued

Note: closures have the same cell
"""
def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x: x + n)
    return adders

print()
adders = create_adders()
print(f'{adders[0](10)=}')
print(f'{adders[1](10)=}')
print(f'{adders[2](10)=}')
print(f'{adders[0].__closure__=}')
print(f'{adders[1].__closure__=}')
print(f'{adders[2].__closure__=}')
print(f'{adders[0](10)=}')

"""
How to solve this problem?

One trick:
"""
def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x + y)
    return adders

print()
adders = create_adders()
print(f'{adders[0](10)=}')
print(f'{adders[1](10)=}')
print(f'{adders[2](10)=}')
print(f'{adders[0].__closure__=}')
print(f'{adders[1].__closure__=}')
print(f'{adders[2].__closure__=}')
print(f'{adders[0].__code__.co_freevars=}')
print(f'{adders[1].__code__.co_freevars=}')
print(f'{adders[2].__code__.co_freevars=}')
print(f'{adders[0](10)=}')
print(f'{adders[0](10, 5)=}')
print(f'{adders[1](10)=}')

#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
#print(f'{=}')
