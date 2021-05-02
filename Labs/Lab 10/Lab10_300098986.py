# Exercise #1:
def allDigits(lst, size):
    if size == 0:
        return True
    elif lst[size - 1] >= 0 and lst[size - 1] <= 9:
        return allDigits(lst, size - 1)
    else:
        return False

# Testing
print(allDigits([1,4,2,3,5],5))
print(allDigits([1,4,21,3,5],5))



# Exercise #2:
def create(L, n):
    if(n == 1):
        L.append(n - 1)
    else:
        create(L, n - 1)
        L.append(n - 1)

def main():
    L = []
    n = int(input("Enter value for n: "))
    create(L, n)
    print(L)

main()


# Exercise #3:
def bcd(x, y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return bcd(y, x)
    else:
        return bcd(y, x % y)

# Testing
print(bcd(1234, 4321))
print(bcd(8192, 192))
