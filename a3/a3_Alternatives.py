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

   ### or
def countMembers(s):
    '''
    (string)->integer
    The function returns the number of extraordinary numbers
    in the string inputted
    '''
    counter = 0
    for char in s: 
        if char in "efghijFGHIJKLMNOPQRSTUVWX23456!\\,":
            counter += 1
    return counter

    ### or
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

######################################################
# Part 2.5
######################################################

def casual_number(s):
    '''
    string -> int
    function has that has one parameter, s, as input where s is a string.
    '''
    
    s = s.replace(',', '')
    return s

######################################################
# Part 2.6
######################################################


def alienNumbers(s):
    '''
    (string)->integer
    The function returns the value of the charaters in a given string as per the NASA value sheet
    Precondition: No onput will be outside of this set {T,y, !,a, N, U}.
    '''
    sum = (s.count("T")*1024)+(s.count("y")*598)+(s.count("!")*121)+(s.count("a")*42)+(s.count("N")*6)+(s.count("U")*1)
    return sum
### OR

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

        b = x + y + z + w + t + k
    return b

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
    '''(string) -> string
    Preconditions: Enter string  
    The function returns a jumbled version of the string entered with the order reversed and the first and last objects placed after one another'''
    l = list(reversed(list(s)))
    m = []
    a = 0
    b = -1
    c = 1
    for i in range(0,len(l)//2,1):
        m.append(l[i])
        m.append(l[b])
        b = b - 1
    return ''.join(m)


######################################################
# Part 2.9
######################################################

def weaveop(s):
    ''''
    (string)->string
    The function returns the string inputted, by inputting either lower case or upper case "op" in between a pair of consecutive characters in a string whether being either lower case or upper case respectively.
    '''
    mod = ""

    for i in range(len(s)-1):
        first = s[i]
        nextt = s[i+1]

        if(first.isalpha()):
            if(first.isupper() and nextt.isalpha()):
                mod += first + "O"
            elif not(first.isupper()) and nextt.isalpha():
                mod += first + "o"
        
        if (nextt.isalpha()):
            if (nextt.isupper()) and first.isalpha():
                mod += "P"
            elif not(nextt.isupper()) and first.isalpha():
                mod += "p"

        if not(first.isalpha() and nextt.isalpha()):
            mod += first
            
    return mod+s[-1]

### OR

def weaveop(string):
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

def nonrepetitive(s):
    '''(string) -> string
    Preconditions: 's' has to be a string
    The function returns whether it has repetitive substrings'''
    l = list(s)
    if len(l) == 0 or len(l) == 1:
        return True
    else:
        for i in range(len(l)-1):
            for j in range(len(l)//2):
                for k in range(len(l)//2):
                    if l[i:i+j+1] == l[i+j:i + j + k + 1]:
                        return False
        l = list(reversed(l))
        for i in range(len(l)-1):
            for j in range(len(l)//2):
                for k in range(len(l)//2):
                    if l[i:i+j+1] == l[i+j:i + j + k + 1]:
                        return False
    return True
### OR

def nonrepetitive(s):
    '''
    (string)->boolean
    The function returns True or False depending on whether the inputted string is nonrepetitive or repetitive respectively. A nonrepetitive word is a word that does not contain any subword twice in a row (A2.pdf)
    '''
    for i in range(1, len(s)):
        substring = s[:i]
        
        if substring * (len(s)//len(substring))+(substring[:len(s)%len(substring)]) == s and s.count(substring)>1:
            return False
    return True

### OR

def nonrepetitive(s):
    """(str) -> bool
    Preconditions: s does not contain spaces.
    Returns whether or not any substring in s repeats consecutively.
    """
    length = len(s)
    state = True
    for i in range(length):
        for j in range(i,length):
            s1 = s[i:j].strip()
            s2 = s[j:2*j - i].strip()
            if s1 == s2 and s1 != "" != s2:
                state = False
            
    return state

### OR

def nonrepetitve(s):
# any word, which can repeat in the string, can only be maximum
# half of the length of the string
# below loop considers all such words starting from length 1    
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
