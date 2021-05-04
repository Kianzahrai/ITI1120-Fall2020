def largest_34(a):
    '''(list) -> (int)
    returns the sum of the 3rd and 4th largest elements in the given list
    '''
    t=0
    s=[]
    while t<len(a):
        if t==2:
            s.append(max(a))
        if t==3:
            s.append(max(a))
        else:
            m=max(a)
            a.remove(m)
        t+=1
    return sum(s)

def largest_third(a):
    '''(list) -> (int)
    return the sum of the (len(a)//3) largest elements in the given list
    '''
    a.sort()
    n=0
    t=[]
    while n<(len(a)//3):
        b=max(a)
        t.append(b)
        a.remove(b)
        n+=1
    return sum(t)

def third_at_least(a):
    '''(list) -> (int),(None)
    return a value in the given list that occurs (len(a)//3+1) times or returns None if no element satisfies the condition
    '''
    for i in a:
        if a.count(i)>=(len(a)//3)+1:
            return i
    return None
    
def sum_tri(a,x):
    '''(list, int) -> (bool)
    returns true if there are three elements in the given list add up to the given integer and false if there isn't
    '''
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            for k in range(len(a)-1):
                if a[i]+a[j]+a[k]==x:
                    return True
    return False
