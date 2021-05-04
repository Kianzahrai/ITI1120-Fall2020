# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

def two_length_run(x): # a version with for loop over indices
     '''(list)-> bool
      Returns True if there is a run of lenght at least 2
      in the list of numbers x and False otherwise.
      Precondition: x is a list of numbers
     '''
     for i in range(len(x)-1):
          if x[i]== x[i+1]:
               return True
     return False
          


def two_length_run_v2(x): # a version with for loop over indices
     '''(list)-> bool
      Returns True if there is a run of lenght at least 2
      in the list of numbers x and False otherwise.
      Precondition: x is a list of numbers
     '''
     result = False
     i = 0
     while i < len(x) - 1 and not result:
       if x[i]== x[i+1]:
            result = True
       i = i + 1
     return result

raw_input = input("Please input a list of numbers separated by space: ").strip().split()
a=[]
for s in raw_input:
     a.append(float(s))
print(two_length_run(a))






