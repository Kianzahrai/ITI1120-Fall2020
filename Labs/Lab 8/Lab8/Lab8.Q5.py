def sort(items):#function declaration
    step_count=0;
    for step in range(len(items)):#steps here for sorting
        # Find the location of the smallest element in
        loc = step
        for location in range(step, len(items)):
            # determine location of smallest
            if items[location] < items[loc]:
                loc = location
                step_count=step_count+1
        # Exchange items[step] with items[loc]
        temporary_item = items[step]
        items[step] = items[loc]
        items[loc] = temporary_item
    print("Steps For take sort:"+str(step_count))#output display
    print("Sorted list::"+str(items));#output display

# To test:
# list1=[5,4,3]#new list here
# sort(list1)#list1 sort here and call it
# list2=[4,3,2]#new list
# list2.sort()#sort it and call
# print(list2)#output display
