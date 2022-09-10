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
            return NotImplemented
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

# Note: this yields TypeError: '<=' not supported between instances of 'Rectangle' and 'Rectangle'
# lte is not automatically implemented
# print(f'{r1<=r2}')



# =======================================================

# Getter and setter -- Java-motivated example
# Motivation: suppose someone tries r1.width = -100
# By directly accessing the property, a user can set it
# incorrectly. We want to implement logic that prevents
# this
class Rectangle:
    # Note: we use the "_" convention to convey that these
    # are private variables, even though the compiler does
    # note enforce this
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    def __str__(self):
        return f'Rectangle: width={self._width}, height={self._height}'

print('\nGetters and setters the un-pythonic way:')
print('r1 = Rectangle(10,20)')
print('r1.width = -100')
r1 = Rectangle(10,20)
r1.width = -100
print('This is NOT pythonic')
print(f'{r1.get_width()=}')
# This will throw an error!
#r1.set_width(-10)

# =======================================================

# Getter and setter -- Pythonic
# Using this strategy, you don't have to create your
# getters and setters at the outset for fear of breaking
# backwards compatibility
class Rectangle:
    # Note: even the __init__ method is calling the getters and setters here!
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height
    
    def area(self):
        return self.width * self._height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'

    def __repr__(self):
        return f'Rectangle({self.width},{self.height})'

print('\nGetters and setters the Pythonic way:')
print('r1 = Rectangle(-10,20) throws a value error')
print('r1.width = -100 throws a value error')
r1 = Rectangle(10,20)
#r1.width = -100
print('r1 = Rectangle(-10,20) throws a value error')
#r1 = Rectangle(-10,20)
