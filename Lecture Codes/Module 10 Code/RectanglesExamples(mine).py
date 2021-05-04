class Rectangle(object):
    '''
    Geometric rectangle
    '''

    def __init_(self, long = 0, wide = 0):
        slef-height = long
        self-width = wide

    def area(self):
        return self.height * self.width

    def display(self):
        print("The height is: ", self.height)
        print("The width is: ", self.width)
        area = self.area
        print("The area is: " area)

# To test:
# rect1 = Rectangle() since no value is given
# rec1.display()
# --> The height is: 0
# --> The width is: 0
# --> The area is: 0
# rect2 = Rectangle(3, 6)

class Point(object):
    '''
    Geometric Point
    '''
    def display(self):
        print("X = ", self.x, "; Y = ", self.y, "; Color = ", self.color)

# pt1 = Point()
# pt1.x = 5
# pt1.y = 8
# pt1.color = 'red'
# pt1.y --> 8
# pt1.display()
# --> X = 5; Y = 8 ; Color = red

class Point(object):
    '''
    Geometric Point
    '''

    def __init__(self, x=0, y=0, color = "red"):
        self.x = x
        self.y = y
        self.color = color

    def equivalent(self, other):
        '''
        (Point, Point) --> bool
        self == other
        if the position and color are the same
        '''
        return self.x == other.x and self.y == other.y and self.color == other.color

    def display(self):
        print("X = ", self.x, "; Y = ", self.y, "; Color = ", self.color)

# pt1 = Point()
# pt1.display()
# pt2 = Point()
# To compare equivalncy:
# pt1.equivalent(pt2) --> True
# Point.equivalent(pt1, pt2) --> True
# The 2 lines above work in the same way
# pt3 = Point(3, 5, "black")
# Point.equivalent(pt1, pt3) --> False

class Point(object):
    '''
    Geometric Point
    '''

    def __init__(self, x=0, y=0, col = "red"):
        '''
        (Point, int, int, str) -->
        '''
        self.x = x
        self.y = y
        self.color = col

    def __repr__(self):
        ''' (Point) --> str'''
        return "Xpt: " + str(self.x) + "Ypt: " + str(self.y) + " color: " + self.color

    def __eq__(self, other):
        '''(Point, Point) --> bool'''
        return self.x == other.x and self.y == other.y and self.color == other.color

    def display(self):
        '''(Point) --> None'''
        print("X = ", self.x, "; Y = ", self.y, "; Color = ", self.color)

class Rectangle(object):
    '''rectangle'''
    def __init__(self, corner, wide, long):
    # corner = rectangle point on the upper left side
    self.corner = corner
    slef.width = wide
    self.length = long

    def info(self):
        '''(Rectangle) --> str'''
        return str(self.corner) + "; Width " + str(self.width) + "; Height " + str(self.height)

    def equivRect(self, other):
        '''(Rectangle, Rectnagle) --> bool'''
        return self.corner == other.corner and self.width == other.width and self.height == other.height

    def findCenter(self):
        '''(Rectangle) --> Point'''
        p = Point()




# pt1 = Point(3, 5)
# pt2 = Point(3, 5)
# pt3 = Point(5, 7)
# pt1 == pt3 --> False
# pt1 == pt2 --> true
# rect1 = Rectangle(pt1, 20, 30)
# rec2 = Rectangle(pt3, 20, 30)
# rec1.equivrect(rec2) --> False
# rec3 = Rectangle(pt2, 20, 30)
# Rectangle.equivRect(rec1, rec3) --> True
# rec4 = Rectangle(Point(4, 5, 'blue'), 20, 30)
# Rectangle.equivRect(rec4, rec3) --> False

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):

# Testing:
# rec = Rectangle(5, 2)
# rec.area() --> 10
# rec.perimeter() --> 14
# sq = Square(4)
# sq.area() --> 16
# sq.perimeter() --> 16
        return 4 * self.length
        

        
