class Person(object): # A person has a last name and first name
    def __init__(self, lastName, firstName):
        self.lastName = lastName
        self.firstName = firstName
    

class Student(object):
    ''' A student has a student number, a midterm mark, a final exam mark and a
        hommework average
    '''

    #Constructor:
    def __init__(self, pers, num, midterm = 0, final = 0, hwAv = 0):
        self.person = pers
        self.studNum = num
        self.midterm = midterm
        self.finalMark = final
        self.hwAver = hwAv
       
    # Methods definition

    def computeMark(self):
      return 0.3*self.midterm + 0.5*self.finalMark + 0.2*self.hwAver


    def displayInfo(self): 
      print(self.person.lastName)
      print(self.person.firstName)
      print("Student number: ", self.studNum)
      print("Midterm mark: ", self.midterm)
      print("Final mark: ", self.finalMark)
      print("Hws average: ", self.hwAver)
      print("Total mark: ", self.computeMark())
      print("Course grade: ", self.distributionMark())
      print()

    def distributionMark(self):
        note = self.computeMark()
        if(note >= 90):
            return "A+"
        elif(note >= 85):
          return "A"
        elif(note >= 80) :
          return "A-"
        elif(note >= 75) :
          return "B+"
        elif(note >= 70) :
          return "B"
        elif(note >= 65) :
          return "C+"
        elif(note >= 60) :
          return "C"
        else :
          return "F"
