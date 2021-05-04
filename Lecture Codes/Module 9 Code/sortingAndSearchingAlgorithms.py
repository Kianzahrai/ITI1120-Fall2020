# is value in the list:
def isValInList(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return True
        return False

# to test it:
# list = [3,6,8,12,47,29]
# find = lisValInList(list, 12)
# print (find)


# counts the occurences of value in a list:
def countOccurVal(aList, value):
    count = 0
    for index in range (len(aList)):
        if aList[index] == value:
            count = count + 1
    return count

# to test it:
# list = [3,6,8,12,47,29]
# total = countOccurVal(list,29)
# (total)


# Index of value in the list with for loop:
def valPosition(aList, value):
    for index in range (len(aList)):
        if aList[index] == value:
            return index # there is a match. Stop
    return -1 # -1 means no match

# to test it:
# list = [3,6,8,12,47,29]
# print (valPosition(list, 12))


# Binary search:
def binary_search(alist, value):
    first, last = 0, len(aList)-1
    while first <= last:
        miffle = (first + last) // 2
        if aList[middle] == value:
            return middle
        elif value > aList[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return -1

# to test it:
# list = [3,5,7,9,11,13,17,21,27,35]
# print(binary(list, 17))


# merge 2 lists:
def merge2Lists1 (alist1, alist2):
    index1, index2 = 0,0 # indexes respectively for alist1 and alist2
    list3 = []

    while (index1 < len(alist1)) and (index2 < len(alist2)):
        if alist1[index1] <= alist2[index2]:
            list3.append(alisr1[index1])
            index1 = index1 + 1
        else:
            lsit3.append(alist2[index2])
            index2 = index2 + 1

    # the while loop will stop if any of the lists is done
    # we do ont know which opne, if alist1 still has data,
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

# to test it:
# list1, list2 = [1,3,8], [2,3,10,12]
# print(merge2Lists1(list1, list2))


def merge2Lists2(alist1, alist2):
    index1, index2 = 0,0
    list3 = []
    while index1 < len(alist1) and index2 < len(alist2):
        if alist1[index1] <= alist2[index2]:
            list3.append(alist1[index1])
            index1 = index1 + 1
        else:
            list3.append(alist2[index2])
            index2 = index2 + 1
    # let us check if there is any data left on aly list:
    for index in range(index1, len(alist1)):
        list3.append(alist1[index1])
    for index in range(index2, len(alist2)):
        list3.append(alist2[index2])
    return list3

# to test it:
# list1, list2 = [1,3,8], [2,3,10,12]
# print(merge2Lists2(list1,list2))
    
def mergeUnique(alist1, alist2): # no duplicates
    index1, index2 = 0,0 # indexes for alist1 and alist2
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

        while index1 < len(alist1):
            if isValLast(list3, alist1[index1]):
                list3.append(alist1[index1])
            index1 = index1 + 1

        while index2 < len(alist2):
            if isValLast(list3, alist2[index2]):
                list3.append(alist2[index2])
            index2 = index2 + 1

        return list3

# to test it:
# list1, list2 = [1,3,8], [2,3,10,12]
# print(mergeUnique(list1, list2))


def isValLast(alist, value):
    pass

def isItKey(dictio, value):
    return value in dictio.keys()

# O(n) - looping over a list of size n:
def displayList(aList):
    for index in range(len(alist)):
        print(alist[index], end = " ")
        # it will loop n times --> o(n)

def displayHalfList(alist):
    for index in range(len(alist),2):
        print(alist[index], end = " ")
        # it will loop n/2 times --> o(n)

# O(n^2): embedded or nested loops, each being
# executed n times:
def displayMatrix(mat):
    for row in mat:
        for col in row:
            print(mat[row][col], end = " ")
        print()
# all together there are n*n steps --> 0(n^2)


# bubble sort function
def bubbleSort1(alist):
    print("Origonal list:", alist,"\n")
    exchange = True # if exchange took place
    while exchange:
        exchange = False # initially + has to change to True to keep looping
        for index in range(len(alist)-1):
            if alist[index] > alist[index+1]: # switch:
                exchange = True
                alist[index], alist[index+1] = alist[index+1], alist[index]
                print(alist)
        print()
    return alist

# to test it:
# list = [5,1,4,2,8]
# print(bubbleSort1(list))


# We can achieve the same objective by moving the max at the end of the list,
# after each iteration, the list decreases by 1 from the right side
def algoSort1(alist):
    print("Origonal list:", alist,"\n")
    for step in range(len(alist) - 1, 0, -1):
        for index in range(step):
            if alist[index] > alist[index+1]: # switch:
                alist[index], alist[index+1] = alist[index+1], alist[index]
                print(alist)
        print()
    return alist

# To test it:
# list = [5,1,4,2,8]
# print(algoSort2(list))


# sorting by insertion
def insertionSort1(alist):
    print("Origional list:", alist,"\n")

    for ref in range(1, len(alist)): # start at ref = 1
        actualValue = alist[ref] # the one to be tested against the others
        index = ref

        while alist[index - 1] > actualValue and index > 0:
            alist[index] = alist[index - 1]
            index = index - 1

        alist[index] = actualValue
        print(alist)

# to test it:
# list = [85,12,59,45,72,51]
# print(insertionSort1(list))


# we can achieve the same objective by moving the min at the start of the list,
# after each iteration, the list decreases by 1 from the left side
def algoSort2(alist):
    print("Origional list:", alist, "\n")
    for ref in range(len(alist) - 1):
        for index in range(ref+1, len(alist)):
            if alist[index] < alist[ref]: # switch
                alist[ref], alist[index] = alist[index], alist[ref]
                print(alist)
        print()
    return alist

# to test it:
# list = [5,1,4,2,8] or list = [5,4,2,8,1,3]
# print(algoSort2(list))


# sorting by selection:
def selectionSort(alist):
    print("Origional list:", alist, "\n")
    for ref in range(len(alist) - 1):
        minPos = ref # store the position
        for index in range (ref + 1, len(alist)): # get the min:
            if alist[index] < alist[minPos]:
                minPos = index

        print("the min =", alist[minPos], "at position:", minPos)
        print("switch position", ref, "with position", minPos)
        # switch:
        alist[minPos], alist[ref] = alist[ref], alist[minPos]
        print(alist,"\n")

    return alist

# to test it:
# list = [5,1,4,2,8] or list = [5,4,2,8,1,3]
# print(selectionSort(list))


# merge sort:
def mergeSort1(alist):
    # produce a temporary list. Each element of the list
    # produces a one element list. We can then start the process of merging

    print('The list to process:\n', alist,"\n")
    temp = []
    for index in range (len(alist)):
        temp.append([alist[index]])
    print('the original temp (made of single lists):\n', temp, '\n')
    
    # the two lists to merge are temp[index] and temp[i + index].
    index = 0
    # If there is at least 2 lists to merge, we do it, and we repeat.
    
    while index < len(temp) - 1:
        list1 = temp[index]
        list2 = temp[index+1]
        newList = merge2Lists2(list1, list2) # previous merge function
        print('the next merged (sorted) list:', newList, 'is appended to temp')
        temp.append(newList)
        print('the operational temp becomes:', temp[index+ 2:]) # remove the 2 merges
        print()
        index = index + 2

    # copy the last element (alist) of temp as a result:
    if len(temp) != 0: # in case the original list was empty
        alist[:] = temp[len(temp)-1] # move result into alist

# to test it:
# list = [9,2,5,3,1,8]
# mergeSort1(list)
# print(list)


# just for illustration purpose
# recursive MergeSort: Used just as an illustration
def mergeSort2(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
    # not finished yet
