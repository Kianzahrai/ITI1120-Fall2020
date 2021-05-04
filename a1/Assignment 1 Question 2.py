import math

def impl2loz(w):
    '''
    non-negative number (w) --> (integer, float)
    A function that says w = l + o/16, where o is < 16, and l is an integer.
    return value is a pair that represents the w-value
    '''
    l = int(math.floor(w))
    o = (w-l)*16
    return (l, o)


