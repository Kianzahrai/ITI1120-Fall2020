# Assingmnet 1
# Kian Zahrai (#300098986) 
# ITI1120

import math

######################################################
# Question 1
######################################################

def quote_maker(quote, name, city):
    '''
    (string, string, string)--> string
    The function returns a sentence as a string,
    which has combined the inputted quote, name, and city of birth
    in a formed sentence
    '''
    return("In the "+city+", a person called "+name+" said '"+quote+"'")

def poem_generator():
    '''
    (none) -> none
    The function will ask the user for a quote, name, and city of birth
    then print the return statement from the quote_maker 
    by first calling it with the given inputs
    '''
    quote = input("Enter the quote: ")
    name = input("Enter your name: ")
    city = input("Enter the city of birth: ")

    print(quote_maker(quote,name,city))

######################################################
# Question 2
######################################################

def impl2loz(w):
    '''
    non-negative number (w) --> (integer, float)
    A function that says w = l + o/16, where o is < 16, and l is an integer.
    return value is a pair that represents the w-value
    '''
    l = int(math.floor(w))
    o = (w-l)*16
    return (l, o)

######################################################
# Question 3
######################################################

def pale(n):
    '''
    A four digit number is inputted as n in function pale --> return answer is True or False
    That number (n) is not pale if and only if it has at least two consecutive digits each equal
    to 3 (so not pale --> __33, _33_, 33__), or if its last digit is divisible by 4 (___4 or 8).
    '''
    last_2_digits = n % 100
    first_2_digits = n // 100
    middle_2_digits = (n // 10) % 100
    last_digit = n % 10
    return not (last_2_digits == 33 or first_2_digits == 33 or middle_2_digits == 33 or last_digit % 4 == 0 or last_digit == 33) 

######################################################
# Question 4
######################################################

def bibformat(author, title, city, publisher, year):
    ''' (string, string, string, string, number)-> string
    Returns function which returns a string in a form
    '''
    bibit = (str(author) + '(' + str(year) + '). ' + str(title) + '. '+ str(city) + ': '+ str(publisher) + '.')
    return bibit

######################################################
# Question 5
######################################################

def bibformat_display():
    ''' (none)-> none
    Returns a function as author, year of publication, publisher and the headquarter city of the publisher
    '''
    title = input ("Enter the title of a book: ")
    author = input ("Enter the name of the author? ")
    year = input ("What year was the book published? ")
    city = input ("Enter the name of the publisher: ")
    publisher = input ("In what city are the headquarters of the publisher? ")
    bibit = ( author + '(' + str(year) + '). ' + title + '. ' + city + ': ' + publisher + "." )
    return bibit

######################################################
# Question 6
######################################################


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

######################################################
# Question 7
######################################################

def funct(p):
    '''
    Our input is p, a positive integer greater than or equal to 11.
    For solving the equation 5^(r^2) - p + 10 = 0, we are solving for r-value
    since p-value is known.
    To solve for r, using algebra, we manipulate the equation.
    '''
    r = math.sqrt(math.log((p-10),5)) 

    print('The solution is '+str(r))


######################################################
# Question 8
######################################################

def gol(n):

    return math.ceil(math.log(n, 2))

######################################################
# Question 9
######################################################

def cad_cashier(price, payment):
     '''
    (number, number) -> number
    Return the change to give back to the customer in canadian dollars,
    given a price and the payment they gave.
    Preconditions: price & payment >= 0, payment >= price. 2nd decimal of
    payment must be a 0 or 5.
    '''
    price = round(price/5,2)*5
    return round(payment-price,2)

######################################################
# Question 10
######################################################

def min_CAD_coins(price, payment):
    '''(number, number) -> number, number, number, number, number
    Preconditions: "price" is a postive float no more than two decimal places and "price" is less than or equal to "payment"
    Returns the coins needed to give customer the change owed'''

    change = cad_cashier(price,payment)
    t = int(change//2)
    l = int(round((change - (t*2)),2)/1)
    q = int((round((change - (t*2) - l),2)/0.25))
    d = int((round((change - (t*2) - l - (q*0.25)),2)/0.1))
    n = int(round(change - (t*2) - l - (q*0.25) - (d*0.1),2)/0.05)
    return (t, l, q, d, n)

######################################################
