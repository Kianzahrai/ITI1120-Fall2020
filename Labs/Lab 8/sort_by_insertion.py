def insert(L, b):
  """ (list, int) -> None
  Precondition: L[0:b] has already been sorted
  Insert L[b] in the correct position in L[0:b + 1].
  >>> L = [3, 4, -1, 7, 2, 5]
  >>> insert(L, 2)
  >>> L
  [-1, 3, 4, 7, 2, 5]
  >>> insert(L, 4)
  >>> L
  [-1, 2, 3, 4, 7, 5]
  """
  step = 0
  # find or insert L[b]
  # start from the end of L[b] and look an element with a lower value
  i = b
  while i != 0 and L[i - 1] >= L[b]:
     i = i - 1
     step += 1
  # move L[b] in the index i, and move the values after i on the right.
  value = L[b]
  del L[b]
  L.insert(i, value)
  return step

def sort_by_insertion(L):
  """ (list) -> None
  Sort the list L in ascending order
  >>> L = [3, 4, 7, -1, 2, 5]
  >>> sort_by_insertion(L)
  >>> L
  [-1, 2, 3, 4, 5, 7]
  """
  i = 0
  NSteps = 0
  while i != len(L):
    NSteps += 1
    otherSteps = insert(L, i)
    NSteps = NSteps + otherSteps
    i = i + 1
  print("Number of steps", NSteps)
