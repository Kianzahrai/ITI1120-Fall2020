def count_m(l, v):
  '''(list, int) -> int
  Returns the number of v occurences in the list" 
  '''
  NSteps = 0
  counter = 0
  for row_val in l:
    for col_val in row_val:
      NSteps += 1
      if col_val == v:
          counter += 1
  print("Number of steps", NSteps)      
  return counter

N = 100

l1 = [ [1,2,3,8], [4,5,6,8,7], [8,9,60]]
print(l1)
print(count_m(l1, 8))
      

