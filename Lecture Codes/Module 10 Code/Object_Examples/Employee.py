class Employee(object):
   'BASIC COMMON Classe OF AN EMPLOYEE'
   nbEmployees = 0

   #Constructor:
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
     print ("Total number of emlpoyees: ", Employee.nbEmployees)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Number: ", self.empNumb, ", Salary ", self.salary)


    
