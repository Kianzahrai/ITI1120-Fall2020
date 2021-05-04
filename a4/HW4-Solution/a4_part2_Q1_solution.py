# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

def number_divisible(x, n): #a version with for loop over elements of the list
     '''(list of ints, int)->int
      Returns the number of elements of the list x that are divisible by n
      '''
     counter = 0
     for num in x:
        if num % n == 0 :
          counter = counter + 1
     return counter

def number_divisible_v2(x, n): #a version with for loop over indices of the list
     '''(list of ints, int)->int
      Returns the number of elements of the list x that are divisible by n
      '''
     counter = 0
     for i in range(len(x)):
        if x[i] % n == 0 :
          counter = counter + 1
     return counter


def number_divisible_v3(x, n): #a version with while loop over indices
     '''(list of ints, int)->int
      Returns the number of elements of the list x that are divisible by n
      '''
     counter = 0
     i = 0
     while i < len(x):
        if x[i] % n == 0 :
          counter = counter + 1
        i = i + 1   
     return counter




raw_input = input("Please input a list of numbers separated by spaces: ").strip().split()
n = int(input("Please input an integer: "))
a=[]
for item in raw_input:
     a.append(int(item))

print("The number of elements divisible by", n, "is", numberDivisible(a, n))






