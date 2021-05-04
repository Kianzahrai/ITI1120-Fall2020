# Actually, square is a rectangle with special features (length = width)

class Rectangle:
    def __init_(self, length, width):
        self.length = length
        self.width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# We thus declare the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# Testing:
# rec1 = Rectangle(3, 8)
# rec1.area() --> 24
# rec1.perimeter() --> 22
# sq1 = Square(5)
# sq1.area() --> 25

# We used super(). to call the __init__() of the Rectanlge class,
# in order to use it in the Square class, without repeating code
# Rectanlge is the superclass, Square is the subclass

# Let us create a class Cube that inherits from Square and extends
# the functionality of .area() (inherited from the Rectanlge class through
# Square class to calculate the surface area and volume of a Cube instance:

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    def volume(self):
        face_area = super().area()
        return face_area * self.length


# Testing:
# cub1 = Cube(4)
# cub1.surface_area() --> 96
# cub1.volume() --> 64

# We could replace the parameterless super() by its equivalent:
# super(Square, self) where the 1st parameter refers to the subclass Square
# and the 2nd one to a Square object, self.
# no difference, only providing clarity on what is happening

class Cube2(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6
    def volume(self):
        face_area = super(Square, self).area()

# Testing:
# cub1 = Cube2(4)
# cub1.surface_area() --> 96
# cub1.volume() --> 64

