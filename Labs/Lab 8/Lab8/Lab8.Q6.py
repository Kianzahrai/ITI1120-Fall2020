def insertionSort(list):
    steps = 0
    for index in range(1,len(list)):
        currentvalue = list[index]
        position = index
        steps = steps + 1
    while position>0 and list[position-1]>currentvalue:
        list[position]=list[position-1]
        position = position-1
        list[position]=currentvalue
        steps = steps + 1
        print(list)
    print("Number of steps: ",steps)

'''
To test: Example:
list = [64,25,12,22,11]
insertionSort(list)
print(list)
'''
