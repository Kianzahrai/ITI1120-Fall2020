# Is value in the List:
def isValIaList(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return True
    return False

#To test it:
# list = [3,6,8,12,47,29]
# total = isValIalist(list, 12)
# print(total)


# Counts the occurences of a vlaue in list:
def countOccurVal(aList, value):
    count = 0
    for index in range(len(aList)):
        if aList[index] == value:
            count = count + 1
    return count

# To test it:
# list = [3,6,8,12,47,29, ]
# total = countOccurVal(list, 29)
# print(total)

# Index of value in the list with for loop:
def valPosition(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return index # there is a match --> stop
    return -1 # -1 --> means no math

# To test it:
# list = [3,6,8,12,47,29, ]
# total = valPosition(list, 3)
# print(total)

#Binary Search
def binary_search(alist, value):
    first, last = 0, len(alist) - 1 # first and last deliminate the section
    while first <= last:
        middle = (first + last) // 2 # find the middle
        if alist[middle] == value: # if found return the position
            return middle
        elif value > alist[middle]: # look on the right
            first = middle + 1
        else: # look on the left
            last = middle - 1
    return -1 # not found

# To test it:
# list = [3, 5, 7, 9, 11, 13, 17, 21, 27, 35]
# print(binary_research(list, 17))

# Merge 2 lists:
def merge2Lists1(alist1, alist2):
    index1, index2 = 0, 0 # indexes respectively for alist1 and alist2
    list3 = []

    while (index1 < len(alist1)) and (index2 < len(alist2)):
        if alist1[index1] <= alist2[index2]:
            list3.append(alist1[index1])
            index = index1 + 1
        else:
            list3.append(alist2[index2])
            index2 = index2 + 1

        # the while loop will stop if any of the lists is done
        # we do not know which one, if alist1 still has data,
        # we append them to alist3:
        while (index1< len(alist1)):
            list3.append(alist1[index1])
            index1 = index + 1


        # if it is alist3 that still has data,
        # we append them to alist3:
        while (index2 < len(alist2)):
            list3.append(alist2[index2])
            index2 = index2 + 1

        return list3

# To test it:
# list = [31.3.8], [2,3,10,12]
# print(merge2Lists1(list1, list2))


def mergeUnique(alist1, alist2): # no duplicates
    index1, index2 = 0, 0 # indexes for both respectively
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
    # we do not know which one, if aist1 still has data,
    # we append them to alist3:
    while index1 < len(alist1):
        if isValLast(list3, alist1[index1]):
            list3.append(alist1[index1])
        index1 = index1 + 1

    # if it is alist3 that still has data
    # we append them to alist3:
    while index2 < len(alist2):
        if isValLast(list3, alist2[index2]):
            list3.append(alist2[index2])
        index2 = iindex2 + 1

#def isValLast():

# Bubble sort
def bubblesort1(alist):
    print("Original list:", alist, "\n")
    exchange = True
    while exchange:
        exchange = False # initially + has to change to True to keep looping
        for index in range(len(alsit)-1):
            if alist[index] > alist[index + 1]: #switch
                exchnage = True
                alist[index], alist[index + 1] = alist[index + 1], alist[index]
                print(alist)
        print()
    return alist

# To test:
# list = [5, 1, 4, 2, 8]
# print(bubbleSort1(list))

# We can achieve the same objective by moving the max at the end of the list,
# after each iteration, the list decreases by 1 from the right side
# needs to be fixed
def algoSort2(alist):
    print("Original list:", alist, "\n")
    for step in range(len(alist) - 1, 0, -1):
        for index in range(step):
            print('index:', index)
            if alist[index] > alist[index + 1]: #switch
                alist[index], alist[index + 1] = alist[index + 1], alist[index]
                print(alist)
            print()
    return alist

# To test:
# list = [5, 1, 4, 2, 8]
# print(algoSort2(list))
# 5, 1, 4, 2, 8 --> # 5, 1, 2, 4, 8
# 5, 1, 2, 4, 8 next line # 1, 5, 2, 4, 8 --> # 1, 2, 5, 4, 8
# last line 1, 2, 4, 5, 8

# We can achieve the same objective by moving the min at the start of the list,
# after each iteration, the list decreases by 1 from the right side
# needs to be fixed
def algoSort3(alist):
    print("Original list:", alist, "\n")
    for ref in range(len(alist) - 1):
        for index in range(ref + 1, len(alist)):
            if alist[index] < alist[index + 1]: #switch
                alist[index], alist[index + 1] = alist[index + 1], alist[index]
                print(alist)
            print()
    return alist

# To test:
# list = [5, 1, 4, 2, 8]
# print(algoSort3(list))
# 5, 1, 4, 2, 8 --> # 5, 1, 2, 4, 8
# 5, 1, 2, 4, 8 next line # 1, 5, 2, 4, 8 --> # 1, 2, 5, 4, 8
# last line 1, 2, 4, 5, 8



# Sorting by Insertion:
def insertionSort1(alist):
    print("Original list:", alist, "\n")

    for ref in range(l, len(alist)): # start at ref = 1
        actualValue = alist[ref] # The one to be tested against the others
        index = ref

        while alist[index - 1 ] > actualValue and index > 0:
            alist[index] = alist[index - 1]
            index = index - 1
        alist[index] = actualValue
        print(alist)

# To test:
# list = [85, 12, 59, 45, 72, 51]
# print(insertionSort1(list))

# Sorting by Selection:
def selectionSort(alist):
    print("Original list:", alist, "\n")
    for ref in range(len(alist) - 1):
        minPos = ref # Store the position
        for index in range(ref + 1, len(alist)): # Get the minimum #
            if alist[index] < alist[minPos]:
                minPos = index

        print("The min =", alist[minPos], "at position", minPos)
        print("switch position", ref, "with position", minPos)
        #switch
        alist[minPos], alist[ref] = alist[ref], alist[minPos]
        print(alist, "\n")
    return alist

# To test:
# list = [5, 1, 4, 2, 8] or [5,4,2,8,1,3]
# print(selectionSort1(list))

# Merge Sort:
def mergeSort1(alist):
    # Produce a temporary list. Each element of the list.
    # produces a one element list. We can start the merging process

    print('The list to process:\n', alist,'\n')
    temp = []
    for index in range(len(alist)):
        temp.append([alist[index]])
    print('The original temp (made of single lists):\n', temp,'\n')

    # The two lists to merge are temp[index] and temp[index + 1]
    index = 0
    # If there is at least 2 lists to merge, we do it, and we repeat.
    while index < len(temp) - 1:
        list1 = temp[index]
        list2 = temp[index + 1]
        newList = merge2Lists2(list1, list2) # previous merge function
        print('The next merged (sorted) list:', newList, 'is appended to temp')
        temp.append(newList)
        print('ten operational temp becomes:' temp[index + 2::]) #remove the 2 merged
        print()
        index = index + 2

    # Copy the last element (a list) of temp as a result:
    if len(temp) != 0: # In case the original list was empty
        alist[:] = temp[len(temp) - 1] # move result into alist

# To test:
# list = [9,2,5,3,1,8]
# print(mergeSort1(list))

    
    
