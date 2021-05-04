# Is value in the list:
def isValIalist(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return True
    return False

# To test it:
# list = [3,6,8,12,47, 29]
# find = isValInList(list, 12)
# print(total)


# Counts the occurences of value in a list:
def countOccurVal(aList, value):
    count = 0
    for index in range(len(aList)):
        if aList[index] == value:
            count = count + 1
    return count

# To test it:
# list = [3,6,8,29,12,47,29]
# total = countOccurVal(list,29)
# print(total)


# Index of value in the list with for loop:
def valPosition(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return index # there is a match. Stop
    return -1 # -1 means no match

# To test it:
# list = [3,6,8,12,47,29]
# print(valPosition(list, 12))



# Binary search:
def binarySearch(alist, value):
	first, last = 0, len(alist) - 1 # first and last delimitate the section searched
	while first <= last:
		middle = (first + last) // 2  # find the middle
		if alist[middle] == value:   # if found return the position
			return middle
		elif value > alist[middle]:  # look on the right
			first = middle + 1
		else: # look on the left
			last = middle - 1
	return -1 # not found

# To test it:
# list = [3, 5, 7, 9, 11, 13, 17, 21, 27,35]
# print(valPosition(list, 17))



# Merge 2 lists:
def merge2Lists1(alist1, alist2):
    index1, index2 = 0,0 # indexes respectively for alist1 and alist2
    list3 = []

    while (index1 < len(alist1)) and (index2 < len(alist2)):
        if alist1[index1] <= alist2[index2]:
            list3.append(alist1[index1])
            index1 = index1 + 1
        else:
            list3.append(alist2[index2])
            index2 = index2 + 1
            
    # the while loop will stop if any of the lists is done
    # we do not know which one, if alist1 still has data,
    # we append them to alist3:
    while (index1 < len(alist1)): 
      list3.append(alist1[index1])
      index1 = index1 + 1

    # if it is alist3 that still has data,
    # we append them to alist3:
    while (index2 < len(alist2)): 
        list3.append(alist2[index2])
        index2 = index2 + 1  

    return list3

# To test it:
# list1, list2 =[1,3,8], [2,3,10,12]
# print(merge2Lists1(list1,list2))


def merge2Lists2(alist1, alist2):
	index1, index2 = 0, 0
	list3 = []
	while index1 < len(alist1) and index2 < len(alist2):
		if alist1[index1] <= alist2[index2]:
			list3.append(alist1[index1])
			index1 = index1 + 1
		else:
			list3.append(alist2[index2])
			index2 = index2 + 1
	# Let us check if there is any data left on any list:
	for index in range(index1, len(alist1)):
		list3.append(alist1[index])
	for index in range(index2, len(alist2)):
		list3.append(alist2[index])
	return list3

# To test it:
# list1, list2 =[1,3,8], [2,3,10,12]
# print(merge2Lists2(list1,list2))


def mergeUnique(alist1, alist2): # no duplicates
    index1, index2 = 0,0 # indexes for alist1 and alist2 respectively
    list3 = []

    while index1 < len(alist1):
        if alist1[index1] <= alist2[index2]:
            if isValLast(list3, alist1[index1]):
                list3.append(alist1[index1])
            index1 = index1 + 1
        else:
            if isValLast(list3, alist2[index2]):
                list3.append(alist2[index2])
            index2 = index2 + 1
            
    # the while loop will stop if any of the lists is done
    # we do not know which one, if alist1 still has data,
    #we append them to alist3:
    while index1 < len(alist1):
        if isValLast(list3, alist1[index1]):
            list3.append(alist1[index1])
        index1 = index1 + 1
      
    # if it is alist3 that still has data,
    # we append them to alist3:
    while index2 < len(alist2):
        if isValLast(list3, alist2[index2]):
            list3.append(alist2[index2])
        index2 = index2 + 1  

    return list3

# To test it:
# list1, list2 =[1,3,8], [2,3,10,12]
# print(merge2Lists2(list1,list2))


def isValLast(alist, value): # Is value at the end of alist:
              size = len(alist)
              # alist should be empty:
              if size == 0:
                  return True
              if (alist[size-1] < value):
                  return True
              return False

# To test it:
# list1, list2 =[1,3,8], [2,3,10,12]
# print(mergeUnique(list1,list2))


               
#Big O Notation:

# O(1) - basic operations: 1 addition/multiplication,
# a function call, accessing a dictionary, a set:
def isItKey(dictio, value):
    return value in dictio.keys()
    

# O(n) - looping over a list of size n:
def displayList(alist):
    for index in range(len(alist)):
        print(alist[index], end = " ")
        # It will loop n times --> O(n)

def displayHalfList(alist):
    for index in range(len(alist),2):
        print(alist[index], end = " ")
        # It will loop n/2 times --> O(n)


# O(log n) - bigger than O(1), but lesser than O(n):
# Binary Search of a list of N elements:
# N/2 + N/4 + N/8 + … + 1 --> O(log_2 N)


# O(n^2): embedded or nested loops, each being
# executed n times:
def displayMatrix(mat):
    for row in mat:
        for col in row:
            print(mat[row][col], end = " ")
        print()
# all together there are n*n steps --> O(n^2) 




# Bubble sort:
def bubbleSort1(alist):
	print("Original list:", alist,"\n")
	exchange = True # if exchange too place
	while exchange:
		exchange = False # initially + has to change to True to keep looping
		for index in range(len(alist)-1):
			if alist[index] > alist[index+1]: # switch:
				exchange = True
				alist[index], alist[index+1] = alist[index+1], alist[index]
				print(alist)
		print()
		
	return alist

# To test:
# list = [5,1,4,2,8]
# print(bubbleSort1(list))


# We can achieve the same objective by moving the min at the start of the list,
# after each iteration, the list decreases by 1 from the left side
def algoSimul11(alist):
    print("Original list:", alist,"\n")
    for ref in range(len(alist) - 1):
	    for index in range(ref+1, len(alist)):
		    if alist[index] < alist[ref]: # switch:
			    alist[ref], alist[index] =  alist[index], alist[ref]
	    print(alist)
	    print()

    return alist

# To test:
# list = [5,1,4,2,8,3]
# print(algoSimul11(list))

# Same as above
def algoSimul22(alist): # use buit-in fct min
    for ref in range(len(alist)-1):
        mini = min(alist[ref:])
        if alist[ref] != min:
            minPos = alist.index(mini)
            alist[ref], alist[minPos] = alist[minPos], alist[ref]
        print(alist)
        print()

# To test:
# list = [5,1,4,2,8,3]
# print(algoSimul22(list))



def algoSimul33(alist): # use buit-in fct max
    for ref in range(len(alist)-1,0,-1):
        maxi = max(alist[:ref])
        if alist[ref] != maxi:
            maxPos = alist.index(maxi)
            alist[ref], alist[maxPos] = alist[maxPos], alist[ref]
        print(alist)
        print()

# To test:
# list = [5,1,4,2,8,3]
# print(algoSimul33(list))



# Soring by Insertion:
def insertionSort1(alist):
    print("Original list:", alist,"\n")
    
    for ref in range(1,len(alist)): # start at ref=1
        actualValue = alist[ref] # The one to be tested against the others
        index = ref

        while alist[index - 1 ] > actualValue and index > 0:
            alist[index] = alist[index - 1]
            index = index - 1

        alist[index] = actualValue
        print(alist)

# To test:
# list = [85,12,59,45,72,51]
# print(insertionSort1(list))



# Sorting by Selection:
def selectionSort1(alist):
	print("Original list:", alist,"\n")
	for ref in range(len(alist) - 1):
		minPos = ref # Store the position
		for index in range(ref + 1, len(alist) ): # Get the min:
			if alist[index] < alist[minPos]:
				minPos = index

		print("The min =", alist[minPos], "at position:", minPos)
		print("switch positon", ref, "with position", minPos)
		# switch:
		alist[minPos], alist[ref] = alist[ref], alist[minPos]
		print(alist,"\n")

	return alist

# To test:
# list = [5,1,4,2,8] or list = [5,4,2,8,1,3]
# print(selectionSort1(list))




# Merge Sort:
def mergeSort1(alist):
    # Produce a temporary list. Each element of the list
    # produces a one element List. We can start the process of merging

    print('The list to process:\n', alist,'\n')
    temp = []
    for index in range(len(alist)):
        temp.append([alist[index]])
    print('The original temp (made of single lists):\n', temp,'\n')
    
    # The two lists to merge are temp[index] and temp[i + 1ndex].
    index = 0
    # If there is at least 2 lists to merge, we do it, and we repeat.
    while index < len(temp) - 1:
        list1 = temp[index]
        list2 = temp[index + 1]
        newList = merge2Lists2(list1, list2) # previous merge fct
        print('The next merged (sorted) list:', newList, 'is appended to temp')
        temp.append(newList)
        print('the operational temp becomes:', temp[index + 2:]) # remove the 2 merged one
        print()
        index = index + 2

    # Copy the last element (a list) of temp as a result:
    if len(temp) != 0: # In case the original list was empty
        alist[:] = temp[len(temp)-1] # move result into alist

# To test:
# list = [9,2,5,3,1,8]
# mergeSort1(list)
# print(list)



# Execution time:

# REMOVE THE print AND return IN ANY OF THE ABOVE ALGORITHMS:
#*******************

def bubbleSort(alist):
	exchange = True # if exchange too place
	while exchange:
		exchange = False # initial
		for index in range(len(alist)-1):
			if alist[index] > alist[index+1]: # switch:
				exchange = True
				alist[index], alist[index+1] = alist[index+1], alist[index]

def mergeSort(alist):
    temp = []
    for index in range(len(alist)):
        temp.append([alist[index]])

    index = 0
    # If there is at least 2 lists to merge, we do it, and we repeat.
    while index < len(temp) - 1:
        list1 = temp[index]
        list2 = temp[index + 1]
        newList = merge2Lists2(list1, list2) # previous merge fct
        temp.append(newList)
        index = index + 2

    if len(temp) != 0: # In case the original list was empty
        alist[:] = temp[len(temp)-1] # move result into alist

def algoSimul1(alist):
    for ref in range(len(alist) - 1):
	    for index in range(ref+1, len(alist)):
		    if alist[index] < alist[ref]: # switch:
			    alist[ref], alist[index] =  alist[index], alist[ref]

def algoSimul2(alist): # use buit-in fct min
    for ref in range(len(alist)-1):
        mini = min(alist[ref:])
        if alist[ref] != min:
            minPos = alist.index(mini)
            alist[ref], alist[minPos] = alist[minPos], alist[ref]

def algoSimul3(alist): # use buit-in fct max
    for ref in range(len(alist)-1,0,-1):
        maxi = max(alist[:ref])
        if alist[ref] != maxi:
            maxPos = alist.index(maxi)
            alist[ref], alist[maxPos] = alist[maxPos], alist[ref]

def insertionSort(alist): 
    for ref in range(1,len(alist)): # start at ref=1
        actualValue = alist[ref] # The one to be tested against the others
        index = ref

        while alist[index - 1 ] > actualValue and index > 0:
            alist[index] = alist[index - 1]
            index = index - 1

        alist[index] = actualValue

def selectionSort(alist):
	for ref in range(len(alist) - 1):
		minPos = ref # Store the position
		for index in range(ref + 1, len(alist) ): # Get the min:
			if alist[index] < alist[minPos]:
				minPos = index
        	# switch:
		alist[minPos], alist[ref] = alist[ref], alist[minPos]

def Sort(alist):
    alist.sort()

#********************
import time, random

def executeTime(dataList, fctList):
    for fct in fctList:
        cop = fctList.copy()
        print(fct.upper()+':')
        start = time.perf_counter()
        eval(fct + '(' + str(dataList) + ')')
        stop = time.perf_counter()
        print(stop - start, '\n')

# To test:
# import time, random, sys
# sample = random.sample(range(5000), 5000)
# fcts = ['bubbleSort', 'mergeSort', 'insertionSort', 'algoSimul1', 'algoSimul2', 'algoSimul3', 'selectionSort', 'Sort']
# executeTime(sample, fcts)
	

def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    print(end_time-start_time)

# To test:
# n = 5000
# sum_of_n_numbers(n)

def executeTime2(dataList, fctList):
    for fct in fctList:
        cop = fctList.copy()
        print(fct.copy()+':')
        start = time.time()
        eval(fct + '(' + str(dataList) + ')')
        stop = time.time()
        print(stop - start, '\n')
# To test:
# import time, random, sys
# sample = random.sample(range(5000), 5000)
# fcts = ['bubbleSort', 'mergeSort', 'insertionSort', 'algoSimul1', 'algoSimul2', 'algoSimul3', 'selectionSort', 'Sort']
# executeTime(sample, fcts)
	

# Errors detected during execution are called
# exceptions and are not unconditionally fatal.
# Some of the known type of exceptions:

# 1/0 --> ZeroDivisionError: division by zero

# if x is not declared:
# 10 * x --> NameError: name 'x' is not defined

# if a variable within an expression is not of appropriate Type:
# 7/'15' --> TypeError: unsupported operand type(s) for /: 'int' and 'str'

# You can't find a file while trying to open it:
# f = open('myfile.txt') --> FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'

# if your input is not of the expected type:
# x = int(input("Please enter a number: "))
# if you key in, for example, y
# --> ValueError: invalid literal for int() with base 10: 'y'


# It is possible to handle selected exceptions (errors): TRY/EXCEPT
# A try clause is executed up until the point where the first exception is
# encountered.
# Inside the except clause, or the exception handler, you determine how the
# program responds to the exception.
# It is possible to anticipate multiple exceptions and differentiate how the
# program should respond to them.

# Division by zero:
def inverse(divisor):
    try:
        x = 1/divisor
        return x
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
    

# File not found:
def readFile(fileName):
    try:
        f = open(fileName)
    except FileNotFoundError as err:
        print("Could not open file:", err)

# Mutiple exceptions:
def processFile(fileName):
    try:
        f = open(fileName)
        s = f.readline()
        i = int(s)
        x = 1/i
        return x
    except FileNotFoundError as err1:
        print("Could not open the file:", err1)
    except ValueError:
        print("Could not convert data to an integer.")
    except ZeroDivisionError as err2:
        print('Handling run-time error:', err2)
    

# You could have an else clause that gets executed if no exception happens:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)

# We could "raise" (throw in Java) our own type of error:

def divide2(x, y):
    try:
        result = x/y
        if result > 5:
            raise Exception('result should not exceed 5.')
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is ", result)
