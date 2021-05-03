import random

def find(list, value):
  '''(list, int) -> bool
  Returns True if value is in the list, False otherwise" 
  '''
  NSteps = 0
  find = False
  for val in list:
      NSteps += 1
      if val == value:
        print("Number of steps", NSteps)
        return True
  return False


n = 100
# list in ascending order from 1 to n
list1 = [ v for v in range(1, n+1) ]
print(list1)
print(find(list1, 78))
      
# list with random elements
list3 = []
for i in range(n):
  v = random.randrange(1,n+1)
  list3.append(v)
print(list3)
print(find(list3, 78))
