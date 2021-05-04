# A function with no parameters/arguments (no return of value)
def table7():
    i = 1 # local variable
    while i < 11 :
        print(i * 7, end =' ')
        i = i + 1
    print()

# To test it: type table7() 

# (2) A function with no parameters/arguments (no return of value)
def table7():
    for index in range(1,11):
        print(index * 7, end =' ') 
    i = 1 # local variable
    while i < 11 :
        print(i * 7, end =' ')
        i = i + 1
    print()

# To test it: type table7() 

# A function with no parameters/arguments but calling another function
def tripleTable7():
    print("The multiplication by 7 in trpilicate:")
    table7()
    table7()
    table7()

# To test it: type tripleTable7() 

# A function with no parameters/arguments but calling another function
def multiplicationTable(base, start, end):
    print("Fragment of the The multiplication by,", base, ':')
    for index in range(start, end + 1):
        print(index, 'x', base, '=', index * base)

# To test it: multiplicationTable(8, 13, 17)

# Local versus global variables:
def mask():
    p = 20 # another p, a local variable
    print(p, q)

# To test it, you must type: p, q = 15, 38
# then type (next line): mask()
# After defining p in shell, the computer will not care, because 20
# is form the memory of function. Only q is new and used
# When calling p in shell after above test, 20 is no longer in memory
# (deleted), instead 15 will be p in this example.


# Local versus global variables:
def increment():
    global p # some action within function bloc concerning p is expected)
    p = p + 1
    print(p)

# To test it, you must type: p = 15
# then type (next line): increment()
# will not accept any other variable
# after many trials of increment (), p becomes the last trial
# number of increment()


# A function with a paramneterand retrun something:
def cube(n):
    return n*n*n

# To test it: cube(4)

# Docstrings/Help-function:
def prime(n):
    '''(int)--> bool returns True if n is prime, False otherwise
    Precondition: n is a positive integer '''
    if(n == 1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
        return True
# To test it: help(prime)

# Civil Eligibility
def isEligible(age, citiizenship, prison):
    '''(int, str, str)->bool
    Returns True if the person is eligible  and False otherwise
    Precondition: 
    '''
    citizenship = citizenship.lower()
    citizneship = citizenship.strip()
    prison = prison.lower()
    prison = prison.strip()
    if((citizenship =='canada' or citizenship =='canadian') and (age >= 18) and (prison == 'no')):
        return True
    else:
        return False
# To test it: isEligible(20, 'CanaDiAn', 'Niet'or 'Nop')
# due to the 2nd and (in function), it can only accept no for prison
# Also: we can use 'age > 17'  which is same as 'age >= 18' for the permission in IF statement

def mask():
    a, b = 50, 60
    return b

a, b = 10, 20
res = mask() # the function is really here when calling it
print(a, b, res)
# To test it, you type: print(res), a and b were first 50 and 60
# then type after above result (next line): print(a, b, res)
# After defining mask in shell, it will only be shown once, after
# calling a and this time, it will follow the 2nd a, b instead (10 and 20)
# When calling res in shell after above test, mask is no longer in memory
# (deleted)


# A function with no parameters/arguments but calling another function
# returns nothing
def multiplicationTable1(base, start, end):
    print("Fragment of the The multiplication by,", base, ':')
    for index in range(start, end + 1):
        print(index, 'x', base, '=', index * base)

# To test it: multiplicationTable1(8, 13, 17)

# A function with no parameters/arguments but calling another function
def multiplicationTable2(baseList, start, end):
    for index in range(len(baseList)):
        multiplicationTable1(baseList[index], start, end)
        print()

# To test it: multiplicationTable2([3,5,8], 13, 17)

# A function with no parameters/arguments but calling another function
def multiplicationTable3(baseList, startList, endList):
    for index in range(len(baseList)):
        multiplicationTable1(baseList[index], startList[index], endList[index])
        print()

# To test it: multiplicationTable3([3,5,8], [4,6,11], [10,12,14])

def my_fct1(aList):
    aList[0:2] = 100, 200 # same as next 2 lines
    # aList[0] = 100
    # aList[1] = 200
# To test it:
# list = [1,2,3,4,5]
# my_fct1(list)
# print(list)

def my_fct2(aValue, aList):
    aList[2] = 100
    aValue = 5
  
# To test it, type:
# value = 4
# list = [5,3,8]
# my_fct2(list)
# print("Value =", value, "List =', list)


# Question
def mask(aValue, aList):
    aValue = aValue + 1
    aList[0] = -2

# To test it, type:
# value, list = 100, [10,20,30,40]
# mask(value, list)
# print("Value =", value, "List =', list)

