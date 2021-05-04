# Display integers a, a+1, a+2, ..., b
def display(a,b):
    x = list(range(a,b+1))
    i = 1
    while(i == 1):
        i = i + 1
        print(x)
    return (i)
        

a = int(input("Please provide a value for a: "))
b = int(input("Please provide a value for b: "))

display(a,b)
