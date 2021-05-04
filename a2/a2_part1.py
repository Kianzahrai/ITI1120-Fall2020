###ITI1120
### Kian Zahrai
### Assignment 2 Part 1


import random
import math

def ascii_name_plaque(name):
    ''' (str)->None
    Draws/Prints name plaque'''
    print()
    print(5*"*"+len(name)*"*"+5*"*")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print("*  "+2*"_"+name+2*"_"+"  *")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print(5*"*"+len(name)*"*"+5*"*")
    print()


def elementery_school_quiz(flag,n):
    #subtraction code
    '''
    The subtraction code: prompted when value 0 is inserted after primary
    question of entering 0 or 1. Generates two random positive, single-digit
    numbers, asking the pupil for the answer to the math problem with
    those two numbers (subtract the second number from the first)
    '''

    if flag == 0:
        count = 0
        for i in range(n):
            a = random.randint(0,10)
            b = random.randint(0,10)
            result = int(input("Question) " + str(a) + "-" + str(b) + ": "))
            if result == a-b:
                count = count+1 
        return count

    #exponentation code
    # The subtraction code: prompted when value 1 is inserted after primary
    # question of entering 0 or 1. Generates two random positive, single-digit
    # numbers, asking the pupil for the answer to the math problem with
    # those two numbers (raise the first number to the power of the second number)
    	
    else: 
        count = 0
        for i in range(n):
            a = random.randint(0,10)
            b = random.randint(0,10)
            result = int(input("Question) " + str(a) + "^" + str(b) + ": "))
            if result == a**b:
                count = count+1 
        return count
    
def high_school_quiz(a,b,c):

    #display equation
    '''
    After finishing up with elementary_school_quiz (after answering questions,
    and checking if it is correct, we move on to this function. This function has
    three parameters representing three real numbers for the coefficients
    of the quadratic equation ax^2 + bx + c = 0. The function displays/prints the
    equation first and then prints its solutions. The function will display the
    correct and meaningful solutions given any three real numbers for coefficients a, b and c.
    '''
    string = ""
    if a != 0:
        string = string + str(a) + "x^2"
    if b != 0:
        if b<0:
            string = string + "-" + str(b) + "x"
        else:
            string = string + "+" + str(b) + "x"
    if c != 0:
        if c < 0:
            string = string + "-" + str(c)
        else:
            string = string + "+" + str(c)
    print(string)

    #calculate solution
    '''
    dis = discriminant
    '''

    dis = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis))  
    if dis > 0:  
        print(" real and different roots ")  
        print((-b + sqrt_val)/(2 * a))  
        print((-b - sqrt_val)/(2 * a))  
      
    elif dis == 0:  
        print(" real and same roots")  
        print(-b / (2 * a))  
    else: 
        print("Complex Roots")  
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)  

#main function

def main():
    #logic for elementery_school_quiz function 
    '''
    This will be the user interaction part of the program. After the previous function quizzes,
    the program will ask you would like another quadratic equation solved. If the input
    is anything but yes. the program terminates by printing a good bye message as in the examples.
    Otherwise (and any form of typing yes should be acceptable, including with lots of white space
    before and after, and with capital letters and lower case letter etc.), as long as pupil answers
    yes, he/she should be asked for the coefficients again and the resulting new quadratic equation should be solved.
    '''

    flag = int(input("Enter 0 for subtraction \n Enter 1 for exponentation: "))
    n = int(input("Enter how many question you want to solve: "))
    res = elementery_school_quiz(flag,n)
    if res == n:
        print("Congratulation! Mia You'll probably get sn A tommorrow. Good Bye Mia!.")
    elif res == n//2:
        print("You did ok Mia, but I know you can do better. Good bye Mia!")
    elif n == 0:
        print("I think you need more practice Mia. Good bye Mia!.")
    #for high_school_quiz
    while(1):
        a = int(input("Enter coefficent  a: "))
        b = int(input("Enter coefficent  b: "))
        c = int(input("Enter coefficent  c: "))
        high_school_quiz(a,b,c)
        y = input("Enter yes to terminate: ")
        y = y.strip()
        if y == "yes" or y == "YES":
            print("Good Bye Mia!")
            break
    
main()
