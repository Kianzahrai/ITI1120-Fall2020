def find_m(list, value):
  '''(list, int) -> bool
  Returns True if value is in the lists, False otherwise" 
  '''
  NSteps = 0
  find = False
  
  for row_val in list:
    if find: #if find is True
      break
    for col_val in row_val:
      NSteps += 1
      if col_val == value:
          find = True
          break
  print("Number of steps", NSteps)      
  return find


n = 100
list1 = [ [1,2,3,12], [4,5,6], [8,9,7] ]
print(list1)
print(find_m(list1, 8))
      

