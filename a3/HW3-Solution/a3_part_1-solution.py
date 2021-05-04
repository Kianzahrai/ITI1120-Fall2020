# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.
#
# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# Assignment Number 3, Part 1

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

def is_up_monotone(N, d):
    '''(str, str) -> bool
    Preconditions: N and d are both look like positive integers and
    the number of digits in N divisible by the integer that d represents. 

    The function returns  True if N and d meet the requiremets specifed in Part 1
    and implied by the provided test cases. 
    Otherwise it returns False. 
    '''
    is_sorted=True
    jump=int(d)
    for i in range(0,len(N),jump):
        if i+jump!=len(N):
            print( N[i:i+jump]+",", end=" ")
        else:
             print(N[i:i+jump])
        if i!=0 and int(N[i:i+jump]) <=int(N[i-jump:i]):
            is_sorted=False
    return is_sorted
        
            
# main
ascii_name_plaque("Welcome to up-monotone inquiry")
name=input("What is your name? ").strip()
ascii_name_plaque(name+", welcome to up-monotone inquiry.")

flag=True
while flag:
    question=input(name+", would you like to test if a number admits an up-monotone split of given size? ")
    # your code to handle varous form of "yes" goes her
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    elif question!='yes' and question!='no':
        print("Please enter yes or no. Try again.")
    else:
        print("Good choice!")
        # your code goes here (i.e ask for a big positive integer)
        num=input("Enter a positive integer: ").strip()
        if not(num.isdigit()) and (num[0]!="-" or "." in num):
            print("The input can only contain digits. Try again.")
        elif int(num)<=0:
            print("The input has to be a positive integer.Try again.")
        else:
            split=input("Input the split. The split has to divide the length of "+num+" i.e. "+str(len(num))+"\n").strip()
            if not(split.isdigit()):
                print("The split can only contain digits. Try again.")
            elif int(num)<=0:
                print("The split has to be a positive integer.Try again.")
            elif len(num) % int(split) != 0:
                print(split, "does not divide", str(len(num))+".", "Try again.")
            else:
                  # make a function call and pass it the three coefficients the user entered
                  if is_up_monotone(num, split):
                      print("The sequence is up-monotone")
                  else:
                      print("The sequence is not up-monotone")

ascii_name_plaque("Good bye "+name+"!")
