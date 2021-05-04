### Test1
### ITI1120
### Kian Zahrai

import math

### Question 1

def atlantic():
    '''
    The user will insert a value (word or number).
    If the number of characters of the value is
    equal to or greater than 9 -->new
    otherwise --> old
    '''    
    sn = input("Please enter your word/number here: ")
    if len(sn) >= 9:
        return 'new'
    else:
        return 'old'
    
### Question 2

def southern():
    n = int(input('Please enter 1 or 2: '))
    while(n != 1 and n != 2):   #the input numebr is being checked if it is correct or not
            print('Invalid input. Enter again please. ')
            n = int(input('Please enter 1 or 2 please: '))
    if(n == 1):
            pound = int(input('Enter a number for weight in pounds: '))
            ounce = float(input('Enter an integer for weight in ounces: '))

            print(str(pound) + ' pound and ' + str(ounce) + ' ounce is (approxiamtely): ', (pound*16 + ounce)*0.02835)

    else:
        name = input('Please enter your name: ')
        stud_numb = int(input('Please enter your student number: '))
        if(len(str(stud_numb)) == 9):    #converting stud_numb from integer to string to be countable
            print(name + ', you have a new student number.')
        else:
            print(name + ', you have an old student number')
    

### Question 3

def pacific(g1,g2,g3):
    '''
    Determining the grades of a student. Inputs are integer values from 0 to 100.
    Output is true or false depedning on meeting criteria from test file.
    '''
    return (g1  >= 50 and g2 >= 50 and g3 >= 50) and (g1 >= 80 or g2 >= 80 or g3 >= 80)

### If perhaps above function does not work (even though I have tested it) please try bottom function:
def pacific(g1, g2, g3):
    # Checking if all three grades are passing
    all_passed = (g1 >= 50) and (g2 >= 50) and (g3 >= 50)
    # Check if at least one grade is an A
    atleast_one_A = (g1 >= 80) or (g2 >= 80) or (g3 >= 80)
    # Return True only if all grades are passing and at least one is an A
    return all_passed and atleast_one_A


### Question 4

def arctic(n):
     '''(int)->bool'''
     if n // 100000 !=0: # 6 digit number
          d1 = n//100000
          d2 = (n %100000)//10000
          d3 = (n %10000)//1000
          d4 = (n %1000)//100
          d5 = (n %100)//10
          d6 = n % 10
          return d1 == d6 and d2 == d5 and d3 == d4
     else: # 4 digit number
          d1 = n//1000
          d2 = (n %1000)//100
          d3 = (n %100)//10
          d4 = n % 10
          return d1 == d4 and d2 == d3
