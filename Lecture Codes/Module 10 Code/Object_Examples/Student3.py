class Student(object):
    ''' Attributs:
            A student has a:
                student#: studNum
                HWs: hwMarks (a list)
                midterm mark: midterm
                final exam mark: finalExam
        Methods:
            A student can perform 2 tasks:
                Compute the total average: computeMark()
                Comoute the HWs average: hwAver()
                Convert the numerical mark into a literal one: finalExam()
                Display the student information: displayInfo() 
    '''

    #Constructor:
    # midterm and finalExam are, if not specified, by default set to zero.
    # Otherwise they take the value that you assigned them.

    def __init__(self, num, midterm = 0, final = 0):
        self.studNum = num
        self.midterm = midterm
        self.finalExam = final
        self.hwMarks = []
       
    # Method Definitions:

    def hwAver(self):
        aver = 0
        for mark in self.hwMarks:
            aver += mark
        return aver/len(self.hwMarks)
        
    def computeMark(self):
        averHws = self.hwAver()
        return 0.3*self.midterm + 0.5*self.finalExam + 0.2*self.hwAver()
    
    def displayInfo(self):
    	print("Student number: ", self.studNum)
    	print("Midterm mark: ", self.midterm)
    	print("Final mark: ", self.finalExam)
    	print("Hws average: ", self.hwAver())
    	print("Total mark: ", self.computeMark())
    	print("Course grade: ", self.finalMark())
    	print()



    def finalMark(self):
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


    
