def classicSum1(nb) :

  sum = 0
  for i in range (nb,0,-1):
      sum = sum + i
      print(sum, end = " ")

  print()
  return sum

def classicSum2(nb) :

  sum = 0
  for i in range (nb+1):
      sum = sum + i
      print(sum, end = " ")

  print()
  return sum
