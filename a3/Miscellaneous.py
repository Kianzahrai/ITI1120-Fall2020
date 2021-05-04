### ITI1120
### Kian Zahrai (300098986)
### Assignment 4 Part 2

import math

######################################################
# Part 2.1
######################################################

def sum_odd_divisors(n):
    '''
    Takes an integer n as input. IF n = 0, Nothing (None) is returned.
    Otherwise, the result returned is the sum of all the positive
    odd divisor of n. 

    '''
    sum = 0
    if n == 0:
        return (None)
    else:
        if n < 0:
            n = -n
        for i in range(1, n+1):
            if n % i == 0 and n % 2 != 0 :
                sum = sum + i;
                
    return sum

######################################################
# Part 2.2
######################################################

def series_sum():
    '''(none) -> integer
    Preconditions: The parameter input when prompted has to be a non-negative integer
    The function adds the all the squared reciprocals until the squared reciprocal of the number that was input'''
    n = int(input("Please enter a non-negative integer: "))
    if n > 0:
        x = 1000
        for i in range(n):
            x = x + 1/((i+1)**2)
        return x
    elif n == 0:
        return 1000
    else:
        return None

######################################################
# Part 2.3
######################################################

def pell(n):
    '''
    (integer)->integer
    The function returns the nth Pell Number, when n (the position) of the number is given. Pell number are defined by a given function. If the n given is negative, None is returned.
    '''
    if n < 0:
        return None
    elif n == 0 or n == 1 or n == 2:
        return n
    elif n > 1:
        first = 1
        nextt = 2
        for i in range(n-2):
            sumPell = 2 * nextt + first
            first = nextt
            nextt = sumPell
        return sumPell

######################################################
# Part 2.4
######################################################

def countMembers(s):
    '''
    (string)->integer
    The function returns the number of extraordinary numbers
    in the string inputted
    '''
    ans = 0
    for x in s:
        if x >= 'e' and x <= 'j':
            ans = ans + 1
        if x >= 'F' and x <= 'X':
            ans = ans + 1
        if x >= '2' and x <= '6':
            ans = ans + 1
        if x == '!' or x == ',' or x == '\\':
            ans = ans + 1
    return ans

######################################################
# Part 2.5
######################################################

def casual_number(s):
    '''(string) -> integer
    Preconditions: To obtain an integer, enter an integer in quatations 
    The function returns the integer entered without the commmas'''
    l = list(s)
    i=0
    negative = 0
    while i < len(l):
        if l[i] == ',':
            l.remove(',')
            i=i
        elif l[i] == '-':
            negative = negative + 1
            if negative > 1:
                return None
            i+=1
        elif int(l[i]) >= 0 and int(l[i]) <= 9:
            i+=1
        else:
            return None
    if (''.join(l).isdigit()) == True:
        return int(''.join(l))
    elif (l[0] in ('-')) and ''.join(l[1:]).isdigit() == True:
        return int(''.join(l))
    else:
        return None

######################################################
# Part 2.6
######################################################
def alienNumbers(s):
    '''
    (string)->integer
    The function returns the value of the charaters in a given string as per the NASA value sheet
    Precondition: No input will be outside of this set {T,y, !,a, N, U}.
    '''
    sum = (s.count("T")*1024)+(s.count("y")*598)+(s.count("!")*121)+(s.count("a")*42)+(s.count("N")*6)+(s.count("U")*1)
    return sum

######################################################
# Part 2.7
######################################################

def alienNumbersAgain(s):
    '''
    (string)->integer
    The function return the value of the characters
    given in a string as per the NASA value sheet.
    Precondition: No onput will be outside of this set {T,y, !,a, N, U}
    '''
    counterT = 0
    countery = 0
    counterX = 0
    countera = 0
    counterN = 0
    counterU = 0

    for char in s:
        if char == "T":
            counterT += 1
        elif char == "y":
            countery += 1
        elif char == "!":
            counterX += 1
        elif char == "a":
            countera += 1
        elif char == "N":
            counterN += 1
        elif char == "U":
            counterU += 1

    return ((counterT*1024) + (countery*598) + (counterX*121) + (countera*42) + (counterN*6) + (counterU))  

######################################################
# Part 2.8
######################################################

def encrypt(s):
    '''
    (string)->string
    The function returns a modified version of the string inputtied s, by a given algorithm.
    '''
    reverse = s[::-1]
    encrypted = ""

    for i in range(0, round(len(s)/2)+1):
        encrypted = encrypted + reverse[i] + reverse[len(s) -1 -i]
    dif = len(encrypted) - len(s)

    if dif>0:
        encrypted = encrypted[:-dif]

    return encrypted
######################################################
# Part 2.9
######################################################

def weaveop(s):
    ''''
    (string)->string
    The function returns the string inputted, by inputting either lower case or upper case "op" in between a pair of consecutive characters in a string whether being either lower case or upper case respectively.
    '''
    weaved_string = ''
    for i in range(0, len(string) - 1):
        weaved_string += string[i]
        if string[i].isalpha() and string[i + 1].isalpha():
            if string[i].isupper():
                weaved_string += 'O'
            else:
                weaved_string += 'o'
        if string[i + 1].isalpha() and string[i].isalpha():
            if string[i + 1].isupper():
                weaved_string += 'P'
            else:
                weaved_string += 'p'
    weaved_string += string[-1]
    return weaved_string

######################################################
# Part 2.10
######################################################

def squarefree(s):
    '''
    any word, which can repeat in the string, can only be maximum
    half of the length of the string
    below loop considers all such words starting from length 1    
    '''
    for i in range(1,int(len(s)/2) + 1):
  
# consider words of length i
        for j in range(len(s)):
    
    # we are considering two words of length i
    # one starts at j and ends at j+i-1
    # other starts at j+i ends at j+i+i-1
    # if they are same, we will return false
    
            if(j+2*i <= len(s)):
  
# if both words are same, return false
                if(s[j:j+i] == s[j+i:j+2*i]):
                    return False
  
# if no words are same, then it means it is nonrepetitve
    return True
