class Student(object):
    '''Attributes:
        A student has a:
            student#: studNum
            HWs average: hwAver
            midterm mark: midterm
            final exam mark: finalExam
        Methods:
            A student can perform 3 tasks:
                Compute the total average: computeMark()
                Convert the numerical mark into a literal one: fianMark()
                Display the student information: displayinfo

        '''
# Methods definition

    def computeMark(self):
        return 0.3*self.midterm + 0.5.self.finalExam + 0.2*self.hwAver

    def displayInfo(self):
        print("Student number: ", self.studNum)
        print("Midterm mark: ", self.midterm)
        print("Fianl mark: ", self.finalExam)
        print("Hws average: ", self.hwAver)
        print("Total mark: ", self.computeMark())
        print("Course grade: ", self.finalMark())
        print()

    def finalMark(self):
        note = self.computeMark()
        if (note >= 90):
            return "A+"
        elif(note >= 85):
            return "A"
        elif(note >= 80):
            return "A-"
        elif(note >= 75):
            return "B+"
        elif(note >= 70):
            return "B"
        elif(note >= 65):
            return "C+"
        elif(note >= 60):
            return "C"
        else:
            return "F"

# To Test:
# stud1 = Student() --> initialization, followed by the assignings
# stud1.studNum = 12345
# check --> stud1.studNum
# stud1.midterm = 70
# stud1.finalExam = 83
# stud1.hwAver = 92
# stud1.displayInfo
# stud2 = stud1
# stud2.displayInfo

# Constructor:
# midterm, finalExam and hwAver are. if not specified,
# by default set to zero
# Otherwise they take the value that you assigned them.

    def __init__(self, num, midterm = 0, final = 0, hw = 0):
        # Association with the attributes'names
        # the parameters without (= 0) are necessary to be assigned to sth
        # others do not have to, since have (= 0)
        self.studNum = num
        self.midterm = midterm
        self.finalExam = final
        slef.hwAver = hw

# Methods Definition:

    def computeMark(self):
        return 0.3*self.midterm + 0.5.self.finalExam + 0.2*self.hwAver

    def displayInfo(self):
        print("Student number: ", self.studNum)
        print("Midterm mark: ", self.midterm)
        print("Fianl mark: ", self.finalExam)
        print("Hws average: ", self.hwAver)
        print("Total mark: ", self.computeMark())
        print("Course grade: ", self.finalMark())
        print()
    
# To Test:
# stud2.studNum = 12345
# check --> stud2.studNum
# stud2.midterm = 70
# stud2.finalExam = 83
# stud2.hwAver = 92
# stud2.displayInfo
# stud3 = Student(43721, 75, 80, 94)
# --> more efficient by including in () of Student
# stud3.displayInfo




    def __init__(self, num, midterm = 0, final = 0):
        # notice no hw = 0 in () above
            # Association with the attributes'names
        # the parameters without (= 0) are necessary to be assigned to sth
        # others do not have to, since have (= 0)
        self.studNum = num
        self.midterm = midterm
        self.finalExam = final
        self.hwMark = []
    
    def hwAver(self):
        aver = 0
        for mark in self.hwMarks:
            aver += mark
        return aver/len(self.hwMarks)

    def computeMark(self):
        averHws = self.hwAver()
        return 0.3*self.midterm + 0.5.self.finalExam + 0.2*self.hwAver

    def displayInfo(self):
        print("Student number: ", self.studNum)
        print("Midterm mark: ", self.midterm)
        print("Fianl mark: ", self.finalExam)
        print("Hws average: ", self.hwAver())
        print("Total mark: ", self.computeMark())
        print("Course grade: ", self.finalMark())
        print()

    def finalMark(self):
        note = self.computeMark()
        if (note >= 90):
            return "A+"
        elif(note >= 85):
            return "A"
        elif(note >= 80):
            return "A-"
        elif(note >= 75):
            return "B+"
        elif(note >= 70):
            return "B"
        elif(note >= 65):
            return "C+"
        elif(note >= 60):
            return "C"
        else:
            return "F"
    
# To Test:
# stud4 = Student(9123456)
# stud4.midterm = 88
# stud4.finalExam = 64
# stud4.hwMarks = [75, 84, 91, 64]
# stud4.display()

# Constructor
# midterm and finalExam, if not specified, by default set to zero
# otherwise they take the value that you assigned them

    def __init__(self, num, midterm = 0, final = 0, hws = []):
        # notice no hw = [] in () above --> still empty
        # Association with the attributes' names
        # the parameters without (= 0) are necessary to be assigned to sth
        # others do not have to, since have (= 0)
        self.studNum = num
        self.midterm = midterm
        self.finalExam = final
        self.hwMarks = hws


    def hwAver(self):
        aver = 0
        for mark in self.hwMarks:
            aver += mark
        return aver/len(self.hwMarks)

    def computeMark(self):
        averHws = self.hwAver()
        return 0.3*self.midterm + 0.5.self.finalExam + 0.2*self.hwAver

    def displayInfo(self):
        print("Student number: ", self.studNum)
        print("Midterm mark: ", self.midterm)
        print("Fianl mark: ", self.finalExam)
        print("Hws average: ", self.hwAver())
        print("Total mark: ", self.computeMark())
        print("Course grade: ", self.finalMark())
        print()

    def finalMark(self):
        note = self.computeMark()
        if (note >= 90):
            return "A+"
        elif(note >= 85):
            return "A"
        elif(note >= 80):
            return "A-"
        elif(note >= 75):
            return "B+"
        elif(note >= 70):
            return "B"
        elif(note >= 65):
            return "C+"
        elif(note >= 60):
            return "C"
        else:
            return "F"
    
# To test:
# stud6 = Student(32885, 84, 92, [77,88,66,90])
# stud6.hwMarks --> [77, 88, 66, 90]
# stud6.display()
# stud6 = Student(32885, 84, 92)
# stud6.hwMarks --> []
# stud6.hwMarks = [20,33,44,55]
# stud6.display()


class Person(object): #A person has a last name and a first name
    def __init__(self, lastName, firstName):
        self.lastName = lastName
        self.firstName = firstName

    def __repr__(self):
        return "Last name: "+ self.lastName +"; firstname: " + self.firstName

# To Test:
# pers1 = Person('John', "Ray")
# pers1.firstName --> John
# pers1.lastName --> 'Ray'

# In another python file:
from Person import *

# you can slo just have one module consisting of
# both classes, without importing

class Student(object):
        '''Attributes:
        A student has a:
            student#: studNum
            HWs average: hwAver
            midterm mark: midterm
            final exam mark: finalExam
        Methods:
            A student can perform 3 tasks:
                Compute the total average: computeMark()
                Convert the numerical mark into a literal one: finalExam()
                Display the student information: displayinfo

        '''
# Constructor
    def __init__(self, pers, num, midterm = 0, final = 0, hwAv = 0):
        # Association with the attributes'names
        # the parameters without (= 0) are necessary to be assigned to sth
        # others do not have to, since have (= 0)
        self.person = pers
        self.studNum = num
        self.midterm = midterm
        self.finalExam = final
        slef.hwAver = hwAv

    # Methods Definition:

    def computeMark(self):
        return 0.3*self.midterm + 0.5.self.finalExam + 0.2*self.hwAver

    def displayInfo(self):
        print("Student number: ", self.studNum)
        print("Midterm mark: ", self.midterm)
        print("Fianl mark: ", self.finalExam)
        print("Hws average: ", self.hwAver)
        print("Total mark: ", self.computeMark())
        print("Course grade: ", self.finalMark())
        print()
    
# To Test:
# pers2 = Person('Palance', "Jack")
# stud2 = Student(pers2, 12345, 83, 72, 89)
# stud2.person
# stud2.dispayInfo
# pers1 = Person("Joe", "Mo")
# stud = Student(pers1, 43357, 88, 91, 82)
# stud.displayInfo()


class Employee(object):
    'Basic Common class of an employee'
    nbEmployees = 0

    #Contructor:
    def __init__(self, name, num, salary):
        self.name = name
        self.empNumb = num
        self.salary = salary
        Employee.nbEmployees += 1

    def remove(self):
        del self.name
        del self.empNumb
        del self.salary
        Employee.nbEmployees -= 1

    def displayNb():
        print("Total number of employees: ", Employee.nbEmployees)

    def displayEmployee(self):
        print("Name: ", self.name, ", Number: ", self.empNumb, ", Salary ", self.salary)

# To test:
# emplo1 = Employee("Jane Fonda", 17824, 66000)
# emplo2 = Employee("Joe Hill", 38824, 55000)
# Employee.nbEmployees --> 2
# emplo3 = Employee("Jack Palance", 138824, 45000)
# Employee.nbEmployees --> 3
# emplo1.displayEmployee()
# emplo2.displayEmployee()
# emplo3.displayEmployee()
# emplo1.name = 'Minh, Taylor'
# emplo1.displayEmployee()
# --> "Name: ", Minh, Taylor, ", Number: ", 17824, ", Salary ", 66000
# emplo1.remove()
# # Employee.nbEmployees --> 1

