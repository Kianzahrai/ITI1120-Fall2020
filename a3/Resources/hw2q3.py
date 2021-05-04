import random
from operator import add, mul


print("This software tests you with 10 questions …… ")
operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))

def performTest(operation):
    correctCounts = 0
    for quiz in range(10):
        op_test = (0, 1)
        x = random.randint(1,9)
        y = random.randint(1,9)
        
        if operation == 0:
            print(x, "+", y, "=?")
            num_1 = int(input())
            ans_1 = x + y
            if num_1 == ans_1:
                print("Correct.")
                correctCounts = correctCounts + 1
            else:
                print("Incorrect.")
                
                
        elif operation == 1:
            print(x, "*", y, "=?")
            num_2 = int(input())
            ans_2 = x*y
            if num_2 == ans_2:
                print("Correct.")
                correctCounts = correctCounts + 1
            else:
                print("Incorrect.")
    return correctCounts
correctCounts = performTest(operation)
print("Score: ", correctCounts)

if correctCounts <= 6 :
    print("Please ask your teacher for help.")
else:
    print("Congratulations!")

      

