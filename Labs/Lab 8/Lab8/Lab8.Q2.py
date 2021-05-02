#Parameters: 2D array, integer
#Function finds how many searches it takes to find integer in 2D array
def find_m(M,v):
    NSteps = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            NSteps += 1
            if M[i][j] == v:
                print("Number of steps: ", NSteps)
                return True
    return False
