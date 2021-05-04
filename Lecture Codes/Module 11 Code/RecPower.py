def recursivePower(nb, p) :# nb**p
    
    if p == 0:
        return 1 # nb**0 = 1
    else:
        return nb * recursivePower(nb, p-1)

# recursivePower(2,4)
# 2 * recursivePower(2,3)
# 2 * 2 * recursivePower(2,2)
# 2 + 2 + 2 + recursivePower(2,1)
# 2 + 2 + 2 + 2 * recursivePower(2,0)
# 2 + 2 + 2 + 2 * 1
