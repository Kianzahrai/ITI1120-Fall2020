def minPos(list):

    posmin = 0
    for index in range(1,len(list)):
        if list[posmin] > list[index]:
            posmin = index

    return posmin
    
