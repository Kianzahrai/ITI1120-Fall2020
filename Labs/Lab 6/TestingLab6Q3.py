return next((True for i in range(len(x)) if (x[i] + x[i - 1] + x[i - 2])==0 and i > 1), False)

'def sum_of_three(x):#Exercise 3
    tinitial=x[0]
    tmiddle=x[1]
    tfinal=x[2]
    i=3
    p=0
    while p<len(x):
        s=tfinal+tmiddle+tinitial
        if s==0:
            return True
        elif s!=0 and i<len(x):
            tinitial=tmiddle
            tmiddle=tfinal
            tfinal=x[i]
            i+=1
        p+=1
    return False


t = (6,7,0,-4,-3,7)
b=sum_of_three(t)
print(b)
