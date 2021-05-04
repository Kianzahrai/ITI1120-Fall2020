from Person import *

class Student(object):
    ''' A student has a student number, a midterm mark, a final exam mark, and a hw average
    '''

    #Constructeur:
    def __init__(self, pers, num, midterm = 0, final = 0, hw = 0):
        self.person = pers
        self.studNum = num
        self.midterm = midterm
        self.finalMark = final
        self.averHws = hw
       
    # Method definition:

    def computeFinalMark(self):
      return 0.3*self.midterm + 0.5*self.finalMark + 0.2*self.averHws


    def displayInfo(self): 
      print (self.person)
      print("Student number: ", self.studNum)
      print("Midterm mark: ", self.midterm)
      print("Final mark: ", self.finalMark)
      print("Hws average: ", self.averHws)
      print("Total mark: ", self.computeFinalMark())
      print("Course grade: ", self.distributionMark())
      print()

    def distributionMark(self):
        note = self.computeFinalMark()
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
