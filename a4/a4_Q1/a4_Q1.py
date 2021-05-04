def number_divisible(l, n):
    count = 0
    for i in range(0, len(l)):
        if l[i] % n == 0:
            count += 1
    return count

s = input("Please input a list of numbers separated by spaces: ")
l = [int(i) for i in s.split(" ")]
n = int(input("Please input an integer: "))
print("The number of elements divisible by",n,"is",number_divisible(l,n))




    a = sorted(w1)
    b = sorted(w2)
    if a == b:
        return True
    else:
        return False
