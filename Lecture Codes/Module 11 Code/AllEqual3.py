def allEqual3(list, high) :
    # start: allEqual3(list, len(list)-1)

    if  high > 0:
        if list[high] != list[0]:
            return False     
        else:
            allEqual3(list, high-1)
		
    return True
