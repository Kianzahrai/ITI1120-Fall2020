def InvertList(list, low, high) :
    # We start with InvertList(list, 0, size_of_list -1)

    if  high - low >0 :
        list[low], list[high] = list[high], list[low]
        InvertList(list, low+1, high-1)
		
    return list
