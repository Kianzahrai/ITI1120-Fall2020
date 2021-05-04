### Assignment 2 Part 2
### Kian Zahrai
### ITI1120

import math

def min_enclosing_rectangle(radius,x,y):
    '''
    (integer,integer,integer) -> None
    Preconditions: The variable 'radius' must be a positive integer
    The functino takes the  parameters and returns
    the smallest axis-aligned rectangle enclosing the circle
    '''

    if radius < 0:
       return None
    else:
       return (x-radius,y-radius)
    '''
    An altenrative solution is to manipulate the comparison instruction
    associated with the variable radius:
    if radius>=0:
        return (x-radius),(y-radius)
    else:
        return None
    '''
    

def vote_percentage(result):
    # creating the substrings list using comprehension + string slicing
    # Counts the number of "yes" and "no" substrings in the input,
    # and returns the fraction of answers which are "yes", assuming at least one vote.
    substrings = [result[i: j] for i in range(len(result)) 
          for j in range(i + 1, len(result) + 1)] 
    
    #print(substrings)
    
    # initializing the variables for taking the count of yes , no and total
    count_yes = 0
    count_no = 0
    total_count = 0
    
    # iterating the list of the substring to count yes and no strings
    for i in substrings:
        if i.lower() == 'yes':
            count_yes = count_yes + 1
        elif i.lower() == 'no':
            count_no = count_no + 1
    
    # summing us to find the total count
    total_count = (count_yes + count_no)
    # if total is not still zero we find the percentage
    if total_count:
        percent_yes = count_yes/total_count
        return percent_yes
    #else return percentage as 0
    else:
        return '0'
    
  
def vote():
   print("Enter the yes, no, abstained votes one by one and then press enter:")
   s = input()
   percentage = vote_percentage(s)
   if percentage == 1:
       print("proposal passes unanimously")
   elif percentage >=2/3:
       print("proposal passes with super majority")
   elif percentage >= 1/2:
       print("proposal passes with simple majority")
   else:
       print("proposal fails")

