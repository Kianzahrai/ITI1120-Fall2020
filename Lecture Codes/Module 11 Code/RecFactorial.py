def factorialRecur(nb): # Keep in mind 0! = 1
    
    if nb == 0: # 0 is the base case
        return 1
    else:
        return nb * factorialRecur(nb-1)

# factorialRecur(4) =
# 4 * factorialRecur(3)
# 4 * 3 * factorialRecur(2)
# 4 * 3 * 2 * factorialRecur(1)
# 4 * 3 * 2 * 1 * factorialRecur(0)
# 4 * 3 * 2 * 1 * 1
