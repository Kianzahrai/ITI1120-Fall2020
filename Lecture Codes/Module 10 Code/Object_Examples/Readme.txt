Student1
Student2 (Constructor introduction)
Student3
Student4
Person
Student5
Person2
Employee
Rectangle
Point1
point2
Point3

Student1:
========
>>> stud1 = Student()
>>> stud1.studNum = 12345
>>> stud1.displayInfo()
Student number:  12345
Midterm mark:  87
Final mark:  77
Hws average:  89
Total mark:  82.39999999999999
Course grade:  A-


Student2:
========
>>> stud2 = Student(34567)
>>> stud2.displayInfo()
Student number:  34567
Midterm mark:  0
Final mark:  0
Hws average:  0
Total mark:  0.0
Course grade:  F

>>> stud2.midterm = 85
>>> stud2.finalMark = 90
>>> stud2.averHws = 75
>>> stud2.displayInfo()
Student number:  34567
Midterm mark:  85
Final mark:  90
Hws average:  75
Total mark:  85.5
Course grade:  A

>>> stud3 = Student(4567, 77, 85, 90)
>>> stud3.displayInfo()
Student number:  4567
Midterm mark:  77
Final mark:  85
Hws average:  90
Total mark:  83.6
Course grade:  A-


Student3:
========
>>> stud4 = Student(13579)
>>> stud4.midterm = 88
>>> stud4.finalMark = 77
>>> stud4.hwMarks = [88, 77, 94, 55]
>>> stud4.displayInfo()

>>> stud5 = Student(13579, 85, 88)
>>> stud5.hwMarks = [88, 77, 94, 55]
>>> stud5.displayInfo()
Student number:  13579
Midterm mark:  85
Final mark:  88
Hws average:  78.5
Total mark:  85.2
Course grade:  A


Student4:
========
>>> stud6 = Student(86421)
>>> stud6.midterm = 75
>>> stud6.finalMark = 83

>>> stud6.hwMarks = [77, 88, 99, 66]
>>> stud6.displayInfo()
Student number:  86421
Midterm mark:  75
Final mark:  83
Hws average:  82.5
Total mark:  80.5
Course grade:  A-

stud7 = Student(135794, 75, 88, [77, 88, 96, 82])
>>> stud7.displayInfo()
Student number:  135794
Midterm mark:  75
Final mark:  88
Hws average:  85.75
Total mark:  83.65
Course grade:  A-


Person:
======
>>> pers1 = Person('Joe', 'Hill')
>>> pers1
Last name: Joe; First name: Hill


Student5:
========
>>> pers2 = Person('Jim', 'Brown')
>>> stud8 = Student(pers2, 1234, 90, 80, 65)
>>> stud8.person
Last name: Jim; First name: Brown
>>> stud8.displayInfo()
Last name: Jim; First name: Brown
Student number:  1234
Midterm mark:  90
Final mark:  80
Hws average:  65
Total mark:  80.0
Course grade:  A-


Person2:
=======
>>> Bob = Person("Robert", "Dali")
>>> stud1 = Student(Bob,12345, 75, 80, 85)
>>> stud1.displayInfo()
Robert
Dali
Student number:  12345
Midterm mark:  75
Final mark:  80
Hws average:  85
Total mark:  79.5
Course grade:  B+


Employee:
========
>>> emp1 = Employee('Joe Hill', 12345, 55000)
>>> emp2 = mployee('edith banker', 8973, 65000)
>>> Employee.displayNb()
Total number of emlpoyees:  2
>>> emp1.displayEmployee()
Name :  Joe Hill , Number:  12345 , Salary  55000
>>> emp2.remove()
>>> Employee.displayNb()
Total number of emlpoyees:  1


Rectangle:
=========
>>> R1 = Rectangle(5, 6)
>>> R1.display()
The height is:  5
the width is:  6
The area is:  30
>>> R1.area()
30
>>> 


Point1:
======
>>> pt1 = Point()
>>> pt1.x = 2
>>> pt1.y= 5
>>> pt1.color = 'blue'
>>> pt1.display()
X =  2 ; Y =  5 ; Color =  blue


Point2:
======
>>> pt2 = Point(3, 5, 'red')
>>> pt3 = Point(3, 5, 'blue')
>>> pt2.equivalent(pt3)
False
>>> Point.equivalent(pt2, Point(3,5,'red'))
True


Point3:
=====
>>> pt1 = Point(3,5)
>>> pt2 = point(3,5)
>>> pt3 = pint(5,7)
>>> pt1 == pt2
True
>>> pt1 == pt3
False

>>> rect1 = Rectangle(pt1, 20, 30)
>>> rect2 = Rectangle(pt3, 20, 30)
>>> Rectangle.equivRect(rect1, rect2)
False
>>> Rectangle.equivRect(rect1, Rectangle(Point(3,5),20, 30))
True

>>> rect1 = Rectangle(Point(4,5,'bleu'), 20, 30)
>>> pt1 = Point(5,3, 'Red')
>>> Rectangle.containedInRect(rect1, pt1)
True

Or
>>> rect1.containedInRect(pt1)
True

Or
>>> rect1 = Rectangle(Point(4,5,'bleu'), 20, 30)
>>> Rectangle.containedInRect(rect1, Point(10,20,"black"))
False
