def displayFormat1():
    # Uses a default precision formula:
    pi, r = 3.1416, 4.7
    ch = "The area of a disk of radius{} is equal to {}."
    print(ch.format(r, pi * r**2)

# --> The area of a disk of radius 4.7 is equal to 69.39794400000001.

def displayFormat2():
    # Uses a 4-digit representation that includes 2 digits
    # for the fractional part:
    pi, r = 3.1416, 4.7
    ch = "The The area of a disk of radius{} is equal to {:4.2f}"
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.40.

def displayFormat3a():
    # Uses a 5-digit representation that includes 2 digits
    # for the fractional part (notice change from 4 to 5 in ch:
    pi, r = 3.1416, 4.7
    ch = "The The area of a disk of radius{} is equal to {:5.2f}"
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.40.

def displayFormat3b():
    # Uses a 5-digit representation that includes 2 digits
    # for the fractional part (notice change from 2f to none in ch:
    pi, r = 3.1416, 4.7
    ch = "The The area of a disk of radius{} is equal to {:5.}"
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.39794400000001.

def displayFormat4():
    # Uses a 6-digit representation that includes 2 digits
    # for the fractional part (notice change from 4 to 5 in ch:
    pi, r = 3.1416, 4.7
    ch = "The The area of a disk of radius{} is equal to {:6.2f}"
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.40.

def displayFormat5():
    # Uses a 6-digit representation that includes 2 digits
    # for the fractional part (notice change from 4 to 5 in ch:
    pi, r = 3.1416, 4.7
    ch = "The The area of a disk of radius{} is equal to {:6.4f}"
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.3979.


def displayFormat6():
    # C tep foratting like:
    col = "green"
    temp = 1.347 + 15.9
    print ("Color %s and temperature %6.2f degreeC" % col, temp))

# --> Color green and temperature 17.25 degreeC

def displayFormat7():
    # C tep foratting like:
    col = "green"
    temp = 1.347 + 15.9
    print ("Color %s and temperature %6.3f degreeC" % col, temp))

# --> Color green and temperature 17.247 degreeC

def list_Strings_Animals():
    # displays the size of each animal in the list
    list = ['dog', 'cat', 'crocodile', 'elephant']
    for animal in list:
        print("size of the chain", animal, '=', len(animal))

""" # -->
size of the chain dog = 3
size of the chain cat = 3
size of the chain crocodile = 9
size of the chain elephant = 8
"""

def 
