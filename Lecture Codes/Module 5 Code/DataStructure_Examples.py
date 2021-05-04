def displayFormat1():
    # Uses a default precision format:
    pi, r = 3.1416, 4.7
    ch = "The area of a disk of radius {} is equal to {}."
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.39794400000001.


def displayFormat2():
    # Uses a 4-digit representation that includes 2 digits for the fractional part:
    pi, r = 3.1416, 4.7
    ch ="The area of a disk of radius {} is equal to {:4.2f}."
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.40.


def displayFormat3():
    # Uses a 4-digit representation that includes 2 digits for the fractional part:
    pi, r = 3.1416, 4.7
    ch ="The area of a disk of radius {} is equal to {:5.2f}."
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.40.


def displayFormat33():
    # Uses a 4-digit representation that includes 2 digits for the fractional part:
    pi, r = 3.1416, 4.7
    ch ="The area of a disk of radius {} is equal to {:5}."
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.40.


def displayFormat4():
    # Uses a 6-digit representation that includes 2 digits for the fractional part:
    pi, r = 3.1416, 4.7
    ch ="The area of a disk of radius {} is equal to {:6.2f}."
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to   69.40.


def displayFormat5():
    # Uses a 6-digit representation that includes 4 digits for the fractional part:
    pi, r = 3.1416, 4.7
    ch ="The area of a disk of radius {} is equal to {:6.4f}."
    print(ch.format(r, pi * r**2))

# --> The area of a disk of radius 4.7 is equal to 69.3979.


def displayFormat6():
    # C type formatting like:
    col = "green"
    temp = 1.347 + 15.9
    print ("Color %s and temperature %6.2f °C" % (col, temp))

# --> Color green and temperature  17.25 °C


def displayFormat7():
    # C type formatting like:
    col = "green"
    temp = 1.347 + 15.9
    print ("Color %s and temperature %6.3f °C" % (col, temp))


def list_Strings_Animals():
    # displays the size of each animal in the list
    list = ['dog', 'cat', 'crocodile', 'elephant']
    for animal in list:
        print("size of the chain", animal, '=', len(animal))


def list_Mixed_Types():
    # displays the type of each element of the list
    mixed = ['snake', 3, 17.25, [5, 'John'] ]
    for element in mixed:
        print(element, type(element))


def repeat_list(n):
    # duplicate a list n times:
    vegetables = ['carrot', 'onion', 'tomato', 'orange']
    print(vegetables * n)



# Note that sort(), reverse replace permanently a list:
# numbers = [17, 38, 10, 25, 72, 12]
# numbers.sort()
# print(numbers) --> [10, 12, 17, 25, 38, 72]
# numbers.reverse()
# print(numbers) --> [72, 38, 25, 17, 12, 10]
# Note:
# rev = numbers.sort()
# print(rev) --> None


# REFERENCE versus COPY in lists:
# fable = ['one','two','three','four', 'five']

# A new reference to fable:
# ref = fable
# print(ref) --> ['fold', 'but','do’, ‘not','break','point']
# They both point to the same memory address
# As such any change done in either one affects both of them:
# ref.append('six')
# print(ref) --> ['one', 'two', 'three', 'four', 'five', 'six']
# print(fable) --> ['one', 'two', 'three', 'four', 'five', 'six']
# fable[3] = 'seven'
# print(fable) --> ['one', 'two', 'three', 'seven', 'five', 'six']
# print(ref) --> ['one', 'two', 'three', 'seven', 'five', 'six']

# Making a copy of a list:
# fable = ['one','two','three','four', 'five']
# copy = [] # empy list
# for element in fable:
#       copy.append(element)
# print(copy) --> ['one','two','three','four', 'five']
# While their content is the same
# fable and copy point at different memory address
# Modifying any one of them does not affect the other one:
# copy.remove('five')
# print(copy) --> ['one', 'two', 'three', 'four']
# print(fable) --> ['one', 'two', 'three', 'four', 'five']


# Tuples, like chains is not changeable:
# Syntax:
# tup = ('a', 'b', 'c', 'd', 'e')
# tup[1] = 'X' --> TypeError: 'tuple' object does not support item assignment
# del tup[0] --> TypeError: 'tuple' object doesn't support item deletion
# to make the chane you need to create a new object while keeping the same name:
# You cannot concatenat tuples:
# tup = ('a','X') + tup[2:]
# print(tup) --> ('a', 'X', 'c', 'd', 'e')
# tup1, tup2 = ("a","b"), ("c","d", 'e')
# tup3 = tup1*2 + tup2
# print(tup3) --> ('a', 'b', 'a', 'b', 'c', 'd', 'e')


# Dictionaries are changeable but not indexed or sequenced
# It is a composite of a key and its value
# Syntax:
def dictionary():
    dict = {} # empty dictionary
    dict['computer'] = 3
    dict['mouse'] = 4
    dict['keyboard'] = 5
    print(dict)
# --> {'computer': 3, 'mouse': 4, 'keyboard': 5}

# print(dico['mouse’]) --> 4

# Another way of creating a dictionary:
# d1 = {'a': 1, 'b': 2, 'c': 3} 
# invent = {'apples': 430, 'bananas': 312, 'oranges' : 274, 'peaches' : 137}

# To remove a key: del invent['apples']
# To add a new key: invent['cucumbers'] = 100
# print(invent) --> {'bananas': 312, 'oranges': 274, 'peaches': 137, 'cucumbers': 100}
# Tot get the value of a key: invent['bananas'] --> 312

# To check if an item exist:
def check(dict, item):
    if item in dict:
        return True
    return False

# To display keys: Use the built-in function keys()
# print(dict.keys() --> dict_keys(['computer', 'mouse', 'keyboard'])
def keys(dict):
    for k in dict.keys(): print(" key :", k, " --- value :", dict[k])

# To display the key values: Use the built-in function values()
# print(dict.values()) --> dict_values([3, 4, 5])

# You can store both keys and values as:
# A list: list(dict.keys()) --> ['computer', 'mouse', 'keyboard']
# A tuple: tuple(invent.values()) --> ( 312, 274, 137, 100)
                                
# Refrencing a dictionary:
# stock = invent  # two references to the same dictionary
# print(stock) --> {'apples': 430, 'bananas': 312, 'oranges': 274, 'peaches': 137}
# stock['peaches'] = 250
# print(stock) --> {'apples': 430, 'bananas': 312, 'oranges': 274, 'peaches': 250}
# print(invent) --> {'apples': 430, 'bananas': 312, 'oranges': 274, 'peaches': 250}

# Copying a dictionary:
# store = stock.copy()
# print(store) --> {'apples': 430, 'bananas': 312, 'oranges': 274, 'peaches': 250}
# store['prunes'] = 350
# print(store) --> {'apples': 430, 'bananas': 312, 'oranges': 274, 'peaches': 250, 'prunes': 350}
# print(store) --> {'apples': 430, 'bananas': 312, 'oranges': 274, 'peaches': 250}

# Going through a dictionary:
# Using for:
# for key in invent: print(key, invent[key])
# for key, value in invent.items(): print(key, value)

# Question: What is the outcome of:
#def f(x):
#    for index in range(len(x)):
#        x[index] = x[index] + 1

# To execute:
# obj = (10,20,30,40)
# f(obj)
# print(obj)


# Sets
# Syntax:
# my_set= {1.0, "Hello", (1, 2, 3)}
# print(my_set) -->  {1.0, 'Hello', (1, 2, 3)}
# set do not have duplicates:
# my_set= {1,2,3,4,3,2}
# print(my_set) -->{1, 2, 3, 4}
# we can make a set from another object (list/tuple) using the built-in set function:
# my_set = set([1,2,3,2])
#print(my_set) --> {1, 2, 3}

# Creating an empty set (tricky):
# initializea with{}: a = {}
# check data type:
# print(type(a)) --> ‘dict’
# then use the fct set: a = set()
# print(type(a)) --> ‘set'

# Sets are mutable. But they are unordered, indexing have no meaning.
# my_set[0] --> TypeError: 'set' object does not support indexing
# We can add single element using the add() method
# and multiple elements using the update() method.
# The update() method can take tuples, lists, strings or other sets as its argument. 

# add an element:
# my_set.add(2)
# print(my_set) -->  {1, 2, 3}

# add multiple elements to a set:
# my_set.update([4,5], {1,6,8})
# print(my_set) -->  {1, 2, 3, 4, 5, 6, 8}

# Going through a Set using "in":
# my_set= {1.0, "Hello", (1, 2, 3)}
# for element in my_set: print(element, end = " ")
# --> 1.0 (1, 2, 3) Hello 

# A particular item can be removed from set using methods, discard() and remove().
# using discard() if the item does not exist in the set, it remains unchanged.
# But remove() will raise an error in such condition.

# Discard an element not present in my_set:
# my_set.discard(10)
# print(my_set) -->  {1, 2, 3, 4, 5, 6, 9}
# my_set.remove(10) --> Output: KeyError: 10

# We can also remove all items from a set using clear().
# my_set.clear()
# print(my_set) -->  set()

# Removing randomly an element with pop():
# print(my_set.pop()) 
