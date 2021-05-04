def dice1(nb):
    import random
    
    sum = -1
    counter = 0
    while nb != sum:
        d1 = int(6*random.random() + 1) # 1 <= d1 <= 6
        d2 = int(6*random.random() + 1) # 1 <= d1 <= 6
        sum = d1 + d2
        counter = counter + 1

    print("We needed to throw the dices",counter,"times to reach the total",nb)



def dice2(nb):
    import random
    
    sum = -1
    counter = 0
    while nb != sum:
        d1 = random.randint(1,6) # 1 <= d1 <= 6
        d2 = random.randint(1,6) # 1 <= d1 <= 6
        sum = d1 + d2
        counter = counter + 1

    print("We needed to throw the dices",counter,"times to reach the total",nb)


def even1(max):
	for nb in range(2,max+1):
		if(nb%2 == 0):
			print(nb,"is even")
		else:
			print(nb,"is odd")


def even2(nb_max):
    for nb in range(2, nb_max+1):
        if nb % 2 == 0:
            print(nb, " is even")
            continue
        print(nb, " is odd")

def Lottery():
  
  import random
  n = 20
  # solution = int(n * random.random()) + 1 # to generate a number between 1 to n
  solution = random.randint(1, n)
  guess = 30
  
  while guess != solution:
      guess = int(input("Enter a new number: "))
      if guess > 0:
          if guess > solution:
              print("Number too big")
          elif guess < solution:
              print("Number too small")
          else:
    	      print("Congratulation you got it!")
      else: # to stop key in a negative nb.
          print("Sorry that you are giving up!")
          break

def MarkDistribution3():

  decision = True

  while (decision):
    s = input("Please enter a grade between 0 and 100: ")
    n = float(s)

    if(n<0 or n>100):
      print("The data is not valid, it is either a negative or a number > 100.")
    elif(n >=90):
      print("The grade is A+")
    elif(n>=85):
      print("The grade is A")
    elif(n>=80) :
      print("The grade is A-")
    elif(n>=75) :
      print("The grade is B+")
    elif(n>=70) :
      print("The grade is B")
    elif(n>=65) :
      print("The grade is C+")
    elif(n>=60) :
      print("The grade is C")
    elif(n>=55) :
      print("The grade is D+")
    elif(n>=50) :
      print("The grade is D")
    elif(n>=40) :
      print("The grade is E")
    else :
      print("The grade is F")

    s = input("Do you want to input another grade (Y/N): ")

    if(s == "N" or s == 'n'):
      decision = False
      print("Bye")

def prime(nb):

    # Prime numbers must be > 1
    if nb > 1:
       # Check for factors?
       for i in range(2,nb):
           if (nb % i) == 0:
               print(nb,"is not a prime number")
               print(i,"times",nb//i,"is equal to",nb)
               break
       else:
           print(nb,"is a prime number")
       
    # if nb is <= 1: it is not a prime number
    else:
       print(nb, "is not a prime number")

def primes(n1, n2):
    for nb in range(n1, n2+1):
        # Prime numbers should be > 1
        if nb > 1:
            #Are there any factors
            for i in range(2,nb):
                if(nb % i) == 0:
                    break

        else:
            print(nb, "is a prime number")

def Product1toN(n):
	prod=1
	counter = 1
	while counter <= n:
		prod = prod*counter
		counter = counter + 1
	return(prod)


def Product1toN2(n):
	prod=1
	counter = n
	while counter > 0:
		prod = prod*counter
		counter = counter - 1 # from n to 1
	return(prod)


def productFrom1toN(n):
    prod = 1
    for x in range(1,n+1):
        prod = prod * x
    return prod


def Sum1toN(n):
	sum = 0
	counter = 1
	while counter <= n:
		sum = sum + counter
		counter = counter+1
	return(sum)

def SumFor(n):
        sum = 0
        for counter in range(1,n+1): # count from 1 to n
            sum = sum + counter
        return(sum)


def TestWhile():

  decision = True # set to True so that we can into
                  # the list at least one (the 1st time)

  while (decision):
    s = input("Please enter a grade between 0 and 100: ")
    n = float(s)

    if(n<0 or n > 100):
      print("The entered note is not valid")
      
    s = input("Do you want to input another grade (Y/N): ")
      
    if(s != "Y" and s != 'y'):
      decision = False
      print("Bye")

