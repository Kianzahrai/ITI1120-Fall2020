def recMinPos(list, posmin, ref):
    #Start: recMinPos(list, 0, 1)

    if list[posmin] > list[ref]:
        posmin = ref

    if ref != len(list)-1:
        return recMinPos(list, posmin, ref + 1)

    return posmin
    
