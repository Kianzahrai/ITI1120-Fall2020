# I understand the importance of professional integrity in my education and future career in

# engineering or computer science. I hereby certify that I have done and will do all work on this

# examination entirely by myself, without outside assistance or the use of unauthorized

# information sources. Furthermore, I will not provide assistance to others.


# Name: Kian Zahrai

# ID: 300098986

def draw_w_stars(n):
    '''(int)->None
    Preconditions: n is positive odd integer
    Draws a figure as depicted in Question 5 with n stars in top and bottom raws
    '''
    for i in range(n):
        if i < n//2 + 1: # upper triangle of figure is printed
            start = i - 1
            final = n - i
            for j in range(n):
                if j <= start or j >= final:
                    print(' ', end = '')
                else:
                    print('*', end = '')
            print('')
        else: # lower triangle of figure is printed
            start = i
            final = n - i - 1
            for j in range(n):
                if j > start or j < final:
                    print(' ', end = '')
                else:
                    print('*', end = '')
            print('')
        


            
    
