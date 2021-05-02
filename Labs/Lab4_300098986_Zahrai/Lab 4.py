### ITI1120
### Kian Zahrai
### Lab 4

import math

### Exercise 1: The Average
def Average(num):

    '''
    Ask for a list of values(num) times 
    from the user, calls the algorithm/function
    and thus computes the average and prints the
    results.
    '''
    numbers = []
    for i in range (0, num):
        x = int(input("Please enter value: "))
        numbers.append(x)

    a = 0
    sum = 0

    #Sum numbers
    while a != len(numbers):
        sum = sum + numbers[a]
        a = a + 1

    #Determine average
    average = sum/len(numbers)

    #return value
    return average
    

### Exercise 2 - Statisitcs calculations
def MarksCalc(num):

    '''
    Ask for values (num) times, which are the
    students’ marks from the user (stored in a list)
    calls function to get the average, the maximum and
    minimum values, while also displaying the results to the user.
    '''
    numbers = []
    for i in range (0, num):
        x = int(input("Please enter value: "))
        numbers.append(x)

    max = 0
    min = 100
    sum = 0
    a = 0

    #Analyze each number, determine max, min, sum
    while a != len(numbers):
        if max < numbers[a]:
            max = numbers[a]
        if min > numbers[a]:
            min = numbers[a]
        sum = sum + numbers[a]
        a = a + 1

    #Find Average
        average = sum/len(numbers)

    #Create list with results
    results = [max, min, average]

    print(results)


### Exercise 3: Ball Toss
def BallToss(velocity):

    '''
    calculates the distance (horizontal, in meters)
    traveled by a ball tossed at v meters per second,
    according to the angle theta (in degres) of the toss.
    '''
#method to calculate distance
def BallToss(v):
    '''
    calculates the distance (horizontal, in meters)
    traveled by a ball tossed at v meters per second,
    according to the angle theta (in degres) of the toss.
    '''
    
    #list to store 10 different distances
    dist = [0]*10
  
    #g will always be 9.8 m/s^2
    g = 9.8
  
    # for all angles i*10
    for i in range(0,9):
  
        #calculating thta in radian
        thetaR = math.pi*i*10/180
  
        #calculating distance with theta = i*10
        distance = 2*v*v*math.cos(thetaR)*math.sin(thetaR)/g
  
        #storing distance in list upto 2 decimals
        dist[i] = "{:.2f}".format(distance)
  
    #returning distance list
    return dist



### Exercise 4: Standard Deviation
    # computes the standard deviation of a list numbers x.
    # Build a code emualting the formula from lab 4 pdf file.
    # Ask for input, generate into list calls the
    # function computes the standard deviation
    # of the values, and displays the results

def standard_deviation(lst):
    m = sum(lst) / len(lst)
    total = 0
    for num in lst:
        total += (num - m) ** 2
    return (total / (len(lst) - 1)) ** 0.5


def main():
    n = int(input("How many numbers do you want to enter? "))
    lst = []
    for i in range(n):
        lst.append(float(input("Enter a number: ")))
    print("Standard deviation is", standard_deviation(lst))


main()
