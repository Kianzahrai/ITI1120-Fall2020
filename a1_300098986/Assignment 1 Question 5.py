def bibformat_display():
    ''' (none)-> none
    Returns a function as author, year of publication, publisher and the headquarter city of the publisher
    '''
    title = input ("Enter the title of a book: ")
    author = input ("Enter the name of the author? ")
    year = input ("What year was the book published?")
    city = input ("Enter the name of the publisher: ")
    publisher = input ("In what city are the headquarters of the publisher?")
    bibit = ( author + '(' + str(year) + '). ' + title + '. ' + city + ':' + publisher + "." )
    return bibit
