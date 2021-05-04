def recursiveSum(nb):
  if nb == 1:
    return 1
  else:
    return nb + recursiveSum(nb - 1)

# recursiveSum(4)
# 4 + recursiveSum(3)
# 4 + 3 + recursiveSum(2)
# 4 + 3 + 2 + recursiveSum(1)
# 4 + 3 + 2 + 1 = 10

