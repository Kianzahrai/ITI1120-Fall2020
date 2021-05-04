def factoClassic(nb) : # Keep in mind that 0! = 1

  fact = 1
  for i in range (nb, 0, -1):
    fact = fact * i
    print(fact, end = ' ')

  print()
  return fact
