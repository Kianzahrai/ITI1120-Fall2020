class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle():
    import math

    def __init__(self,bottomleft=0,topright=0,color="red"):
        '''(Rectangle,number,number,str)->None
        '''
        self.b = bottomleft
        self.t = topright
        self.c = color

    def __repr__(self):
        '''(rectangle)->str
        '''
        return 'Rectangle({},{},"{}")'.format(self.b,self.t,self.c)

    def __str__(self):
        '''(Rectangle)->str
        '''
        return 'I am a {} rectangle with bottom left corner at {} and top right corner at {}.'.format(str(self.c),str(self.b),str(self.t))

    def __eq__(self,other):
        '''(Rectangle,Rectangle)->bool
        '''
        
        return self.b==other.b and self.t==other.t

    def get_bottom_left(self):
        '''(Rectangle)->tuple
        '''
        return self.b 

    def get_top_right(self):
        '''(Rectangle)->tuple
        '''
        return self.t

    def get_color(self):
        '''(Rectangle)->tuple
        Returns the color of the rectangle
        '''
        return self.c

    def reset_color(self,newcol):
        '''(Rectangle,str)-> None
        '''
        self.c=newcol

    def move(self,dx,dy):
        '''(Rectangle,number,number)->None
        '''
        Point.move(self.b,dx,dy)
        Point.move(self.t,dx,dy)

    def intersects(self,other):
        '''(Rectangle,Rectangle)->bool
        '''
        if self.t.x < other.b.x or other.t.x < self.b.x or self.t.y < other.b.y or other.t.y < self.b.y:
            return False
        return True

    def get_perimeter(self):
        '''(Rectangle)->int
        '''
        l=(self.t.x-self.b.x)
        w=(self.t.y-self.b.y)
        return 2*(l+w)

    def get_area(self):
        '''(Rectangle)->int
        '''
        l=(self.t.x-self.b.x)
        w=(self.t.y-self.b.y)
        return l*w

    def contains(self,x,y):
        '''(self,number,number)->bool
        '''
        return (x>=self.b.x and x<=self.t.x) and (y>=self.b.y and y<=self.t.y)
        

class Canvas:

    def __init__(self):
        '''(Canvas)->None
        '''
        self.l=[]

    def __repr__(self):
        '''(Canvas)->lst
        '''
        return 'Canvas('+str(self.l)+' )'
    
    def count_same_color(self,color):
        '''
        (Canvas,str)->int
        '''
        a=0
        for i in self.l:
            t=i.get_color()
            if t==color:
                a += 1
        return a
    
    def min_enclosing_rectangle(self):
        x,y,x1,y1=0,0,0,0
        for i in self.l:
            t=i.get_top_right()
            s=i.get_bottom_left()
            s1=s.get()
            t1=t.get()
            if t1[0]>x:
                x=t1[0]
            if t1[1]>y:
                y=t1[1]
            if s1[0]<x1:
                x1=s1[0]
            if s1[1]<y1:
                y1=s1[1]
        s='Rectangle({},{},"{}")'.format((Point(x1,y1)),(Point(x,y)),"blue")
        return eval((s))

    def __len__(self):
        '''(Canvas)->int
        '''
        return len(self.l)
    def common_point(self):
        ''''''
        for i in range(len(self.l)):
            for j in range(i+1,len(self.l)):
                if i!=len(self.l)-1:
                    t=self.l[i].intersects(self.l[j])
                    if t==False:
                        return False
        return t
            
        

    def add_one_rectangle(self,rectangle):
        '''(canvas,Rectangle)->None
        '''
        self.l.append(rectangle)


    def total_perimeter(self):
        '''(Canvas)->number
        '''
        t=0
        for i in self.l:
            t=t+i.get_perimeter()
        return t
