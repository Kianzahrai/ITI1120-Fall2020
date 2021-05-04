### Exercise 1

def sumList(l):
    sum = 0
    index = 0
    while index < len(l):
        sum = sum + l[index]
        index = index + 1
    return sum
a = [10, 28, -5, 6, 31, 25, -7, 20]
print(sumList(a))


### Exercise 2

def exceed(x, v):
    "Returns True if the sum of the list elements exceede v"
    return sumList(x) > v

a = [10, 28, -5, 6, 31, 25, -7]
print(exceed(a, 100))


### OR
def exceed(x, v):
"Returns True if the sum of the list elements exceed v"
    sum = 0
    index = 0
    while (index < len(x)) and (sum <= v):
        sum = sum + x[index]
        index = index + 1
    return sum > v

a = [10, 28, -5, 6, 31, 25, -7]
print(exceed(a, 100))

### Exercise 3

def countK(x, k):
    "count the number of k in the list"
    count = 0
    for val in x:
        if val == k:
        count = count + 1
    return count
a = [10, 28, -5, 6, 31, 25, 10, -7, 10]
print(countK(a, 10))

### Exercise 4a
def found(x, k):
    "Returns True if k is in the list, else False"
    found = foundK(x,k) > 0
    return found


a = [10, 28, -5, 6, 31, 25, 10, -7, 10]
print(found(a, 10))
print(found, 26))



### Exercise 4b
def found(x, k):
    "Returns True if k is in the list, False else"
    found = False
    for val in x:
        if val == k:
            found = True
            break
    return found
a = [10, 28, -5, 6, 31, 25, 10, -7, 10]
print(found(a, 10))
print(found(a, 26))


#Is value in the list? (A lesser efficient)
def isValueInList2(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            flag = True
            break
        return flag


#Is value in the list? (A more efficient)
def isValueInList3(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return True
        return False
# To test:
# list = [3, 6, 8, 12, 47, 29]
# Flag = isValueInList2(list, 29) or isValueInList3(list, 29)
# print(flag)


# Is value in the list with a while loop:
def isValueInList4(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return True
        else:
            index = index + 1
    return False


def isValueInList4(aList, value):
    index = 0
    while index < len(aList):
        if aList[index] == value:
            return True
        else:
            index = index + 1
        return False


# Use of "in" operator (much more compact)
def isValueInList5(aList, value):
    return value in aList
# To test:
# list = [3, 6, 8, 12, 47, 29]


#Index of value in the list with for loop:
def valuePositionWhile(aList, value):
    for index in range(len(aList)):
        if aList[index] == value:
            return index # there is a match. STOP
        index = index + 1
    return -1 # this means there is no match

# To test:
# list = [3, 6, 8, 12, 47, 29]
# print(valuePositionWhile(list, 12))

#Index of multiple "value" found in the list with for loop:
def valueMultiplePositionWhile(aList, value):
    positions = [] # empty list
    for index in range(len(aList)):
        if aList[index] == value:
            positions.append(index)
    return positions
# To test:
# list = [3, 6, 8, 12, 47, 29]
# storage = (valueMultiplePositionsFor(list, 12)
# if len(storage) > 0:
# print(storage)
# else: print("There is no instance of that value")


# Get the max of a list:
def getMaxList1(aList):
    max = aList[0]
    for index in range(1, len(aList)):
        if aList[index] > max: #only
            max = aList[index]
    return max

# To find the max test:
# list = [3, 6, 8, 12, 47, 29]
# maximum = getMaxList1(list)
# print(maximum)

# Get the max of a list using while loop:
def getMaxList2(aList):
    max = aList[0]
    index = 1
    while index < len(aList):
        if aList[index] > max: #only
            max = aList[index]
        index = index + 1
    return max

# To find the max test:
# list = [3, 6, 8, 12, 47, 29]
# max = getMaxList2(list)
# print(maximum)

# Get the max of a list using only "in":
def getMaxList3(aList):
    max = aList[0]    
    for value in aList:
        if value > max:
            max = value
    return max

# To find the max test:
# list = [3, 6, 8, 12, 47, 29]
# max = getMaxList3(list)
# print(maximum)


# Get the min of a list:
def getMinList1(aList):
    min = aList[0]
    for index in range(1, len(aList)):
        if aList[index] < min: #only
            min = aList[index]
    return min

# To find the min test:
# list = [3, 6, 8, 12, 47, 29]
# minimum = getMinList1(list)
# print(minimum)

# Get the min of a list using only "in":
def getMinList3(aList):
    min = aList[0]    
    for value in aList:
        if value < min: #notice different greater sign convention
            min = value
    return min

# To find the min test:
# list = [3, 6, 8, 12, 47, 29]
# min = getMinList3(list)
# print(minimum)

# Get the min of a list using while loop:
def getMinList3(aList):
    min = aList[0]    
    while index < len(aList):
        if aList[index] > min:
           min = aList[index]
        index = index + 1
    return min

# To find the min test:
# list = [3, 6, 8, 12, 47, 29]
# min = getMinList3(list)
# print(minimum)


# Looking for any duplicates in a list --> double loop:
def hasDuplicate1(aList):
    for ref in range(len(aList)-1): # Reference moves from 0 to length (or size 0 - 2
        for value in range(ref + 1, len(aList)): # value is from reference + 1 to - 1
            if aList[ref] == aList[value]: # A match is found, STOP
                return True
    return False # Reached only if a match has not been found

# Is there a duplicate in the list test:
# list = [19, 22, -15, 11, 15, 22, 36]
# flag = hasDuplicate1(list)
# print(flag)


# testing the list list[:x] and other ones: (to be test with a list with a duplicate)
def test(aList):
    print("The original list", aList)
    for ref in aList[: len(aList) - 1]: # reference from 0 to length - 2
        print(ref, "will be mathced with:")
        for value in aList[aList.index(ref) + 1: len(aList)]:
        # ref is the same in line 3 of this function (from reference + 1 --> length - 1
            print(value, end = " ")
        print()

# To test:
# list = [19, 22, -15, 11, 15, 22, 36]
# test(list)


# Duplicate Implementation
def hasDuplicate2(aList):
    for ref in aList[: len(aList) - 1]: # reference from 0 to length - 2 (the - 1)
        for value in aList[aList.index(ref) + 1: len(aList)]: # value is from reference + 1 to - 1
            if ref == value: # A match is found, STOP
                return True
    return False # Reached only if a match has not been found

# Is there a duplicate in the list test:
# list = [19, 22, -15, 11, 15, 22, 36]
# list = [19, 22, -15, 11, 15, 36]
# flag = hasDuplicate2(list)
# print(flag)


# Looking for any duplicates in a list --> while loop:
def hasDuplicate3(aList):
    ref = 0 #declare, initialize the indexes used
    while ref < len(aList) - 1: # Reference moves from 0 to length (or size 0 - 2)
        value = ref + 1
        while value < len(aList): # value is from reference + 1 to - 1
            if aList[ref] == aList[value]: # A match is found, STOP
                return True
            value = value + 1
        ref = ref + 1
    return False # Reached only if a match has not been found

# Is there a duplicate in the list test:
# list = [19, 22, -15, 11, 15, 22, 36]
# list = [19, 22, -15, 11, 15, 36]
# flag = hasDuplicate3(list)
# print(flag)


