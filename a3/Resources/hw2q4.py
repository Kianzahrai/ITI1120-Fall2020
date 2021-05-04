import random

def doTest(operation):
    x = random.randint(1,9)
    y = random.randint(1,9)

    if operation == 0:
            print(x, "+", y, "=?")
            ans = x + y
        
    elif operation == 1:
            print(x, "*", y, "=?")
            ans = x*y
    guess = int(input())
    if guess == ans:
        smtg = True
    elif guess != ans:
        smtg = False
        print("The correct answer is " + str(ans))
    return (smtg)
    
responsesCorrect = 0
print("The software will process a test with 10 questions …… ")
for compteur in range (10):
    operation = random.randint(0,1)
    if doTest(operation) == True:
         responsesCorrect += 1
print(responsesCorrect, "Correct responses")         
if responsesCorrect  <= 6 :
  print("Ask some help from your instructor.")
else:
  print("Congratulations!")
