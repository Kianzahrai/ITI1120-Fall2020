def binary_search(L, v):
  """ (list, int) -> bool
  Returns True if v is in the sorted list L, False otherwise.
  >>> binary_search([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 10)
  Number of steps 3
  True
  >>> binary_search([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 6)
  Number of steps 4
  False
  """
  NSteps = 0
  find = False
  # i and j cover the search area
  i = 0
  j = len(L) - 1 
  while i != j + 1:
    NSteps += 1
    m = (i + j) // 2  # get the midle
    if L[m] == v:   # if we found it, returns the position
      find = True
      break
    elif L[m] < v:  # look on the right 
      i = m + 1
    else:           # look on the left
      j = m - 1
  print ("Number of steps", NSteps)    
  return find
