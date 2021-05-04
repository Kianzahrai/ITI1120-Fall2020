
def compound(x,y,z):
    '''
    Not allowed to use if statements, so:
    we directly use logical operators and find the result
    and return it
    the first part of logical expression states
    whether x is the only even number second part states
    if any of the pairs adds up to number greater than 100 finally we combine
    them using 'and' operator
    '''
    return (x % 2 == 0 and y % 2 != 0 and z % 2 != 0) and (x+y > 100 or x+z> 100 or y+z> 100)







