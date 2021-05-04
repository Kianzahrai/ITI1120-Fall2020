### ITI1120
### Kian Zahrai
### Assingnment 4 Part 1

import math

###########################################
### 1 Part 1: up-monotone inquiry
###########################################

def is_up_monotone(X, d):
  '''
    (string, string)->boolean
    The function takes as input a number X, and the number of digits of seperation in that number, breaks down the number by that seperation and outputs either True or False on whether the sequeunce is increasing or not.
    Precondition: X and d are positive integers inputted as strings
    Checks if the X is with split d is up_monotone or not
    '''
  div = int(len(X)/int(d))
  start = 0
  end = d
  p=[]
  while div>0:
    p.append(X[int(start):int(end)])
    start = int(start) + int(d)
    end = int(end) + int(d)
    div = div - 1
  
  print(','.join(p))
  if sorted(p) == p:
    print("True. The sequence is up-monotone!")
  else:
    print("False. The sequence is not up-monotone!")

###########################################
### 2 Part 1: User Interface
###########################################
  '''
  a sequence of numbers --> The function prints that sequence of
  numbers in such a way that the consecutive numbers are separated
  by commas as shown in the test cases, except after the last number
  in the sequence. The function returns True if the sequences is up-monotone
  and False otherwise.
  '''

if __name__ == "__main__":
  print("*************************************")
  print("**")
  print("*__Welcome to up-monotone inquiry__*")
  print("**")
  print("*************************************")
  Name = str(input("What is your name? "))
  print("*************************************")
  print("**")
  print("*__",Name,",Welcome to up-monotone inquiry__*")
  print("**")
  print("*************************************")
  flag=True
  while flag:
    question = input(Name+", would you like to test if a number admits an up-monotone split of given size? ")
    if question.lower()=='yes':
      print("Good choice!")
      num = input("Enter a positive integer: ")
      if num.isdigit():
        print("Input the split. The split has to divide the length of "+num+" i.e.,"+str(len(num)))
        d = int(input())
        if len(num)%d == 0:
          is_up_monotone(num,d)
        else:
          print("does not divide ",len(num),". Try again.")
      elif '.' in num:
        print("The input can only contain digits. Try again.")
      elif num.lstrip("-").isdigit():
        print("The input has to be a positive integer.Try again.")
      else:
        print("The input can only contain digits. Try again.")
    elif question.lower()=='no':
      print("*************************************")
      print("**")
      print("*__Good bye ",Name,"__*")
      print("**")
      print("*************************************")
      break
    else:
      print("Please enter yes or no. Try again.")
