### Exercise 5
### input variable is string type, so add the
### quotation marks before and after desired variable
### takes a character chain str and returns another chain
### with spaces inserted between the neighboring letters
def Spaces(str):
    return " ".join(str)

def Spaces2(str):
    NNstr = ""
    for i in range(len(str)):
        if str[i] != " ":
            NNstr = NNstr + str[i] + " "
    NNstr = NNstr.strip()
    return NNstr
            
