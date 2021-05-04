def allEqual2(list, high) :
    # start: allEqual2(list, len(list)-1)

    if  high > 0:
        if list[high] == list[0]:
            allEqual2(list,high-1)
        else:
            return False
		
    return True
