import random

# This function mathces with the lab exercise
def findInt(L, v):
    Nsteps = 0
    for i in range(len(L)):
        Nsteps = Nsteps + 1
        if L[i] == v:
            print('Number of steps:', Nsteps)
            return True
    print('Number of steps:', Nsteps)
    return False


def main():
    L = random.sample(range(1, 1000), 800)
    print(findInt(L, 765))
