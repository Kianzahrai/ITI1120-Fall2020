#classic factorial
def factoClassic(nb):
    # Keep in mind
    # 0! = 1
    fact = 1
    for i in range(nb, 0, -1):
        fact = fact * i
        print(fact, end = " ")
    print()
    return fact

# Recursive method
def factorialRecur(nb):
    if nb == 0:
        return 1
    else:
        res = nb * factorialRecur(nb-1)
        return res
# Testing:
# factorialRecur(4)
# 4 * factorialRecur(3)
# 4 * 3 * factorialRecur(2)
# 4 * 3 * 2 * factorialRecur(1)
# 4 * 3 * 2 * 1 * factorialRecur(0)
# 4 * 3 * 2 * 1 * 1 = 24


def RecursiveSumList1(list):

    size = len(list)
    if size == 1:
        return list[size - 1] # list[0] --> smallest index
    else:
        return list[size - 1] + RecursiveSumList1(list[:size - 1])
    # the last slicing is from 0 to size - 1
        
def RecursiveSumList2(list, low):
    # start with low = 0: RecursiveSumList2(l, 0)
    if low == len(list) - 1:
        return list[low] # list[size - 1]: highest index
    else:
        return list[low] + RecursiveSumList2(list, low + 1)
# Testing
# list = [1, 5, 8, 3]
# RecursiveSumList2(list, 0)

def RecursiveSumList3(list):
    size = len(list)
    if size == 1:
        return list[size - 1] # list[0]
    else:
        return list[0] + RecursiveSumList3(list[1:])
    # the last slicing is from 1 to the end

def RecursiveSumList4(list, high):
    # start with high = len(list) - 1
    # --> RecursiveSumList4(list, len(list)
    if high == 0:
        return list[high] # list[size - 1]: highest index
    else:
        return list[high] + RecursiveSumList4(list, high - 1)


def classicSum1(nb):

    sum = 0
    for i in range(nb, 0, -1):
        sum = sum + i
        print(sum, end = " ")

    print()
    return sum

def classicSum2(nb):

    sum = 0
    for i in range(nb + 1):
        sum = sum + i
        print(sum, end = " ")

    print()
    return sum

# in recursive methods, cannot go 2 ways
# as shown above

def recursiveSum(nb):
    if nb == 1:
        return 1
    else:
        return nb + recursiveSum(nb-1)


# Testing:
# recursiveSum(4)
# 4 + recursiveSum(3)
# 4 + 3 + recursiveSum(2)
# 4 + 3 + 2 + recursiveSum(1)
# 4 + 3 + 2 + 1 = 10
# no recursiveSum(0) since no it has no value
# to increase the result

# Classic method
def ClassicPower(nb, p):
    # nb**p
    result = 1
    for i in range(p, 0, -1):
        result = nb * result
        print(result, end = " ")

    print()
    return result

# Recursive method
def recursicePower(nb, p):
    # nb**p
    if p == 0:
        return 1
    else:
        return nb * recursivePower(nb, p-1)

# Testing:
# recursivePower(2,4)
# 2 * recursivePower(2,3)
# 2 * 2 * recursivePower(2,2)
# 2 * 2 * 2 * recursivePower(2,1)
# 2 * 2 * 2 * 2 * recursivePower(2,0)
# 2 * 2 * 2 * 2 * 1 = 16


def InvertList(list, low, high):
    # We start with InvertList(list, 0, size_of_list - 1)

    if high - low > 0:
        list[low], list[high] = list[high], list[low]
        InvertList(list, low + 1, high - 1)
    return list
# Testing:
# list = [1, 22, 30, 56, 72, 81]
# InvertList(list, 0, len(list) - 1)
# --> [81, 72, 56, 30, 22, 1]
# list = [1, 22, 30, 56, 72, 81, 120]
# InvertList(list, 0, len(list) - 1)
# --> [120, 81, 72, 56, 30, 22, 1]
# notice that 56 does not change position

def allEqual2(list, high):
    # start: allEqual2(list, len(list) - 1)
    if high > 0:
        if list[high] == list[0]:
            allEqual2(list, high - 1)
        else:
            return False
    return True

# Testing:
# list = [1, 2, 2, 4]
# allEqual2(list, len(list) - 1)
# --> False

def allEqual3(list, high):
    # start: allEqual3(list, len(list) - 1)
    if high > 0:
        if list[high] != list[0]:
            return False
        else:
            allEqual3(list, high - 1)
        return True
    
# Testing:
# list = [1, 2, 2, 4]
# allEqual3(list, len(list) - 1)
# --> False

def recBinarySearch(list, value, start, end):
    # Working with a sorted list
    # start with recBinarySearch(list, val, 0, list_size - 1)

    if end - start > 1:
        mid = (end + start) // 2
        if list[mid] == value:
            return True
        else:
            if value < list[mid]: # look on the left
                return recBinarySearch(list, value, start, mid - 1
            else:
                return recBinarySearch(list, value, mid + 1, end)
    else:
        result = (list[start] == value or list[end] == value)
        return result

# Testing:
# list = [1, 2, 5, 7, 99, 15, 29]
# recBinarySearch(list, 100, 0, len(list) - 1)
# --> False

#classical
def minPos(list):

    posmin = 0
    for index in range(1, len(list)):
        if list[posmin] > list[index]:
            posmin = index
        else:
            pass
    return posmin

#recursive
def recMinPos(list, posmin, ref):
    # start: recMinPos(list, 0, 1)

    if list[posmin] > list[ref]:
        posmin = ref
    else:
        pass
    if ref != len(list) - 1:
        return recMinPos(list, posmin, ref + 1)
    return posmin

# Testing:
# list = [11, 23, 4, 76, 3, 9]
# recMinPos(list, 0, 1)
# --> 4

