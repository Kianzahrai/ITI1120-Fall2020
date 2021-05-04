### ITI1120
### Kian Zahrai (300098986)
### Assignment 4 Part 2

import math

######################################################
# Part 2.1
######################################################

def sum_odd_divisors(n):
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
        if x == '!' or x == ',' or x== '\\':
            ans = ans + 1
    return ans
