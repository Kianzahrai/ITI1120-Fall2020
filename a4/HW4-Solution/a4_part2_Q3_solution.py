# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

def longest_run(x):
     '''(list)-> int
      Returns the length of the longest run in the list of numbers x.
      Precondition: x is a list of numbers
     '''
     if len(x)==0: return 0
     
     i = 0
     max_length = 1
     while i < len(x)-1 :
        length = 1
        while  i < len(x)-1 and x[i] == x[i+1]:
           length = length + 1
           i = i + 1
        if length > max_length:
           max_length = length  
        i = i + 1   
     return max_length

raw_input = input("Please input a list of numbers separated by space: ").strip().split()
a=[]
for s in raw_input:
     a.append(float(s))
print(longest_run(a))





