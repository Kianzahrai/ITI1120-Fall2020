def bibformat(author, title, city, publisher, year):
    ''' (string, string, string, string, number)-> string
    Returns function which returns a string in a form
    '''
    bibit = (str(author) + '(' + str(year) + '). ' + str(title) + '. '+ str(city) + ': '+ str(publisher) + '.')
    return bibit
