import random

def count(l, v):
  '''(list, int) -> int
  Count the number of v occurrences in the list" 
  '''
  NSteps = 0
  counter = 0
  for val in l:
      NSteps += 1
      if val == v:
          counter += 1
  print("Number o steps", NSteps)      
  return counter

N = 100
    
# list with random elements
l3 = []
for i in range(N):
  v = random.randrange(1,N+1)
  l3.append(v)
print(l3)
print(count(l3, 3))
