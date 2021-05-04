def list_work(l): # 10 points
     '''(list of int)->list of int

     The function returns a new list where for every pair of consecutive elements in l
     if both are odd or both are even then the sum of the two elements is added to the new list
     otherwise zero is added to the new list. For example, in a list l=[1, 7, 5, 4, 12],
     1 and 7 are both odd, so we add their sum, 8, to the new list
     7 and 5 are both odd, so we add their sum, 12, to the list
     5 and 4 are neither both odd nor both even, so we add zero to the list
     4 and 12 are both even, so we add their sum, 16,  to the list.
     Thus the function returns the list [8, 12, 0, 16]
     
     If l has at most 1 element, then a copy of list l is returned

     >>> list_work([1, 7, 5, 4, 12, -33, 6])
     [8, 12, 0, 16, 0, 0]
     >>> list_work([1])
     [1]
     >>> list_work([])
     []
     >>> list_work([1,2,3,4,5])
     [0, 0, 0, 0]
     >>> list_work([100,20,30])
     [120, 50]
     '''

for index in range(len(l)-1):
    if l[index] % 2 == 1 and l[index + 1] % 2 == 1:
        new_l.append(l[index] + l[index + 1]) 
                
    elif l[index] % 2 == 0 and l[index + 1] % 2 == 0:
        new_l.append(l[index] + l[index + 1])

    else:
        new_l.append(0)

return new_l

        
