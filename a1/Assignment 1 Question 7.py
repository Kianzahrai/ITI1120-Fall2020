import math

def funct(p):
    '''
    Our input is p, a positive integer greater than or equal to 11.
    For solving the equation 5^(r^2) - p + 10 = 0, we are solving for r-value
    since p-value is known.
    To solve for r, using algebra, we manipulate the equation.
    '''
    r = math.sqrt(math.log((p-10),5)) 

    print('The solution is '+str(r))
