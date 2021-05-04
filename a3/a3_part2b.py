#Family name: Maryam Fatima 
# Student number:  0300071011
# Course: IT1 1120 
# Assignment Number 2

import math
########################
# Question 1
########################
def min_enclosing_rectangle(radius, x, y):

    """ (int, int) -> (int, int)
The function should return the x- and y-coordinates of the bottom-left
corner of that rectangle. """
    xcoordinate = x-radius
    ycoordinate = y-radius

    if x < 0 or radius < 1 or y < 0 :
      print("None")
    else:
            return (xcoordinate, ycoordinate)
        
########################
# Question 2
########################
def series_sum():
    """ (int -> int)
prompts the user for an non-negative integer n. If the user enters a negative
integer the function should return None otherwise the function should return
the sumer of the following series 1000 + 1/^1 etc for the given integer n. """

    x = int(input("Please enter a non-negative integer:"))
    if x < 0:
        return None
    elif x > 0:
        for i in range(0,x):
            sum = 1000+ (1/((i+1)**2))
        return sum
    elif x == 0:
        return 1000
    
########################
# Question 3
########################
def pell(n):
    """(int -> int)
Write a function called pell that takes one integer parameter n, of
type int. If n is negative, pell returns None. Else, pell returns
the nth Pell number """
    
    if n < 0:
        print ("NONE")
    elif n == 0:
        p = 0
    elif n == 1:
        p = 1
    else:
        p = 2*pell(n-1) + pell(n-2)
    return p

########################
# Question 4
########################

def countMembers(s):
    '''
    (int or float) -> (int)
    function called countMembers that takes a single input parameter s,
    of type str. countMembers then returns the number of characters in
    s, that are extraordinary
    '''
    a = 0

    for z in s:
        if z >= "e":
            a = a + 1
        if z >= "j":
            a = a + 1
        if z >= "F":
            a = a + 1
        if z >= "X":
            a = a + 1
        if z >= "2":
            a = a + 1
        if z >= "6":
            a = a + 1
        if z == "!":
            a = a + 1
        if z == ",":
            a = a + 1
        if z == "\\":
            a = a + 1
            
        return a
    

########################
#       Question 5
########################

def casual_number(s):
    """ string -> int
function has that has one parameter, s, as input where s is a string. """
    
    s = s.replace(',', '')
    return s

########################
#       Question 6
########################
def alienNumbers(s):
    """string -> int
This function takes one string parameter s, and returns the
integer value represented by s. """

    i = 0
    for char in s:

        x = 0
        y = 0
        z = 0
        w = 0
        t = 0
        k = 0

        if (s.count("T")) >= 0:
            x = (s.count("T")*1024)
        if (s.count("y")) >= 0:
            y = (s.count("y")*598)
        if (s.count("!")) >= 0:
            z = (s.count("!")*121)
        if (s.count("a")) >= 0:
            w = (s.count("a")*42)
        if (s.count("N")) >= 0:
            t = (s.count("N")*6)
        if (s.count("U")) >= 0:
            k = (s.count("U")*1)

        b = x+y+z+w+t+k
    return b

        
########################
#       Question 7
########################
"""string -> int
that takes a single string parameter s, and returns the numeric value of
the number that s represents in the alien numbering system"""

def alienNumbersAgain(s):
     answer = 0
     for b in y:
         if z is "T":
             answer = answer + 1024
             if z is "y": 
                answer = answer + 598
                if z is "!":
                    answer = answer + 121
                    if z is "a":
                        answer = answer + 42
                        if z is "N":
                            answer = answer + 6
                            if z is "U":
                                answer = answer + 1
                                return answer 

    


########################
#       Question 9
########################

""" string -> string
That takes a single string parameter (s) and returns a string."""

def oPify(s):
        for t in range(len (s) -1, 0, -1):
            if s[t].isalpha() and s[t-1].isalpha():
                op= ""
            if s[t-1].isupper():
                op += "o"
            else:
                op += "o"
            if s[t].isupper ():
                op +="p"
            else:
                op += "p"
            s = s[:t] + op + s[t:]
        return s
     

    
