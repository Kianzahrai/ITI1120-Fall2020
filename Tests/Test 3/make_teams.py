# I understand the importance of professional integrity in my education and future career in

# engineering or computer science. I hereby certify that I have done and will do all work on this

# examination entirely by myself, without outside assistance or the use of unauthorized

# information sources. Furthermore, I will not provide assistance to others.


# Name: Kian Zahrai

# ID: 300098986

def make_teams(players, num_teams):
    '''(list of str, int)->2D list
    Make num_teams teams out of the players in list players by counting off.
    Players is a list of players' names and num_teams is the desired number of teams
    Return a 2D list where each sublist is representing a team.
    Preconditions: num_teams>= 1

    >>> make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 3)
    [['pele', 'venus', 'lionel'], ['maradona', 'fed'], ['serena', 'rafa']]
    >>> make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 2)
    [['pele', 'serena', 'fed', 'lionel'], ['maradona', 'venus', 'rafa']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3)
    [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)
    [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 4)
    [['1', '5', '9'], ['2', '6'], ['3', '7'], ['4', '8']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 7)
    [['1', '8'], ['2', '9'], ['3'], ['4'], ['5'], ['6'], ['7']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 11)
    [['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], [], []]
    >>> make_teams( [] , 3)
    [[], [], []]
    '''

   final_list = [] #used to store the list of teams
   for num in range(num_teams): #loop through teams
       temp_list = [] #temp list to store player names in a team
       # loops through player list with a jump of 'num_teams'
       for index in range(num,len(players),num_teams):
           temp_list.append(players[index]) #update temp_list
        final_list.append(temp_list) #update final_list
    return final_list #return result





