"""
The bool class

Python has a concrete bool class that is used to represent Boolean values

However, the bool class is a subclass of the int class

i.e. they possess all the properties and methods of integers, and add some
specialized ones such as and, or, etc.

Two constants are defined: True and False

They are singleton objects of type bool

(i.e. the constant points to a particular memory address)

However, note that True and 1 are not the same objects
"""

print(f'{issubclass(bool, int)=}')
print(f'{isinstance(True, bool)=}')
print(f'{isinstance(True, int)=}')
print(f'{type(True)=}')
print(f'{int(True)=}')
print(f'{True is 1=}')
print(f'{True==1=}')
print(f'{True > False=}')
print(f'{(1==2) == False=}')
print(f'{(1==2) == 0=}')
print(f'{True+True+True=}')
print(f'{(True+True+True)%2=}')
print(f'{-True=}')
print(f'{100*False=}')
print(f'{hex(id(True))=}')
print(f'{hex(id(1+1==2))=}')
print(f'{hex(id(False))=}')
print(f'{hex(id(1+1==3))=}')

"""
The Boolean constructor bool(x) returns True
when x is True

Sounds like a useless constructor, but it is not at all

Many classes contain a definition of how to cast instances of themselves to a Boolean
i.e. a "truth value" or "truthyness"

For integers:
bool(0) -> False
bool(x) -> True for any int x != 0
"""
print(f'\n{bool(0)=}')
print(f'{bool(1)=}')
print(f'{bool(100)=}')
print(f'{bool(-1)=}')

print(f'{type(3<4)=}')
print(f'{None is False=}')
print(f'{1 == 2 == False=}')

print(f'{1+True=}')