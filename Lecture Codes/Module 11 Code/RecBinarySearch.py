def recBinarySearch(list, value, start, end) :
    # We are working on a sorted list
    # We start with recBinarySearch(list, val, 0, list_size - 1)

    if  end - start >1 :
        mid = (end + start)//2
        if list[mid] == value:
            return True
        else:
            if value < list[mid]: # Look on the left
                return recBinarySearch(list, value, start, mid - 1)
            else: # Look on the right
                return recBinarySearch(list, value, mid + 1, end)

    else: 
        result = (list[start] == value or list[end] == value)
        return result

