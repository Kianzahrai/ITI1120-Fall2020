def digit_sum(n):
    '''
    (int)->int
    '''
    if n==0:
        return 0
    return n%10 + digit_sum(n//10)

def digital_root(n):
    '''(int)->(int)'''
    l=[int(x) for x in str(digits_sum(n))]
    if len(l)==1:
        return l[0]
    elif len(l)>1:
        s=sum(l)
        return digital_root(s)
        
    
