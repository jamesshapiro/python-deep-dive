# initialization and properties
class Rectangle:
    # this actually runs after the object has been created
    def __init__(self, width, height):
        self.width = width
        self.height = height

print('properties examples:')
r1 = Rectangle(10,20)
print(f'{r1.width=}')
print(f'{r1.height=}')

r1.width = 100
print(f'{r1.width=}')

# =======================================================

# methods
class Rectangle:
    # this actually runs after the object has been created
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(10,20)
print('\nmethods examples:')
print(f'{r1.area()=}')
print(f'{r1.perimeter()=}')

print('\nno __str__ or __repr__ method defined example:')
print(f'{str(r1)=}')
print(f'{hex(id(r1))=}')

# =======================================================

# string representation
class Rectangle:
    # this actually runs after the object has been created
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'

    def __repr__(self):
        return f'Rectangle({self.width},{self.height})'

r1 = Rectangle(10, 20)
print('\nstr example:')
print(f'{str(r1)=}')
print('\nrepr example:')
print(f'{r1=}\n')

r2 = Rectangle(10, 20)

# returns False because by default equality checks for memory addresses
print('no __eq__ method defined example:')
print(f'{r1=}')
print(f'{r2=}')
print(f'{r1 == r2=}')

# =======================================================

# comparisons
class Rectangle:
    # this actually runs after the object has been created
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.area() < other.area()

    def __repr__(self):
        return f'Rectangle({self.width},{self.height})'

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(10, 30)

print('\n__eq__ and __lt__ examples:')
print(f'{r1=}')
print(f'{r2=}')
print(f'{r3=}')

# still tests for equality of memory address
print(f'{r1 is r2=}')
# uses defined __eq__ method
print(f'{r1 == r2=}')

# this will throw an error if the isinstance clause is not there
print(f'{r1 == 100=}')

print(f'{r1 < r2=}')
print(f'{r1 < r3=}')