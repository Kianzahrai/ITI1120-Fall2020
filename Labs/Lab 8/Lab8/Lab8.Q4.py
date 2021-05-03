#Inputs 2D Array and integer
#Tracks number of times integer appears in 2D array
#Returns number of times it appears
def binary_search(lst, number):
    left, right = 0, len(lst)-1
    count = 0
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if number == lst[mid]:
            print("Number of steps " + str(count))
            return True
        elif number < lst[mid]:
            right = mid-1
        else:
            left = mid+1
    print("Number of steps " + str(count))
    return False
