
def quote_maker(quote, name, city):
    '''
    (string, string, integer)--> string
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
