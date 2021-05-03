
def count(l, v):
    no_of_occurence = 0
    Nsteps = 0
    for i in l:
        if i == v:
            no_of_occurence = no_of_occurence + 1
        Nsteps = Nsteps + 1
  
    print("Number of steps: ", Nsteps)
  
    return no_of_occurence
