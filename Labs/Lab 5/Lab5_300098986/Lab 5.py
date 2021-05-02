### ITI1120
### Kian Zahrai
### Lab 5

### Exercise 1
### each variable assinged to specific characters
### python expressions are derived as instructed
### by the pdf file of lab 5 regarding this exercise
def Chains1():
    str1 = "Good"
    str2 = "Bad"
    str3 = "Crazy"

    if 'azy' in str3:
        print ("There is \'azy\' in \'crazy\'")
    else:
        print ("There is not \'azy\' in \'crazy\'")

    if ' ' in str1:
        print ("There is a space in \'Good\'")
    else:
        print ("There is not a space in \'Good\'")

    print ("The concatenation of all strings is", str1 + str2 + str3)

    if ' ' in str1 + str2 + str3:
        print ("There is a space in the concatenation of all strings")
    else:
        print ("There is not a space in the concatenation of all strings")
    
    print("Crazy repeated 10 times: ", str3 * 10)

    print ("The number of chars in all chains: ",len(str1) + len(str2) + len(str3))


### Exercise 2
### variable assinged to the specific value
### derived python expressions are followed
def Chains2():

    aha = 'abcdefgh'

    if 'abcd' in aha:
        print ("\'abcd\' is in variable")
    else:
        print ("\'abcd\' is not in variable")
    if 'def' in aha:
        print ("\'def\' is in variable")
    else:
        print ("\'def\' is not in variable")
    if 'h' in aha:
        print ("\'h\' is in variable")
    else:
        print ("\'h\' is not in variable")
    if 'fg' in aha:
        print ("\'fg\' is in variable")
    else:
        print ("\'fg\' is not in variable")
    if 'defgh' in aha:
        print ("\'defgh\' is in variable")
    else:
        print ("\'defgh\' is not in variable")
    if 'adg' in aha:
        print ("\'adg\' is in variable")
    else:
        print ("\'adg\' is not in variable")
    if 'bd' in aha:
        print ("\'bd\' is in variable")
    else:
        print ("\'bd\' is not in variable")

### ALTERNATIVE METHOD
def Exercise2():

    # declare the variable aha
    aha = 'abcdefgh'

    # slice the first 4 characters from the variable and assign to a
    a = aha[:4]
    # slice from the 3rd position to the 6th position excluding the 6th character
    b = aha[3:6]
    # get the last character which starts from -1
    c = aha[-1]
    # get from 3rd last character to the end
    d = aha[-3:-1]
    # get from 5th last character to the end
    e = aha[-5:]
    # get from 3rd last character to the end
    f = aha[-3:]
    # get from first character to 7th character with a gap of 3 characters
    g = aha[0:7:3]
    # get from position 1 to 4th position skipping 2 characters(third element within the bracket is the skip value)
    h = aha[1:4:2]

    # printing the results
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)  
        
### Exercise 3
### expression from From by Victor Hugo’s novel «Les miserables»
### followed by the instruced expressions
def Chains3():
    str = ''' In 1815, M. Charles-François-Bienvenu Myriel
    was a bishop in Digne. He was a seventy five years old man; he
    held that position in Digne since 1806. …  '''
    
    nStr = str.replace('.',' ').replace(',',' ').replace(';',' ')
    print(nStr)
    nStr = nStr.strip()
    print (nStr)
    nStr = nStr.lower()
    print (nStr)
    count = nStr.count('in')
    print('\"in\" occurs',count,' number of times' )
    nStr = nStr.replace ('was','is')
    print (nStr)

### Exercise 4
### deriving number of occurrences of a character via 2 versions
# using the count method for class of string
def Count_1(str,c):
    return str.count(c)

# using the for loop
def Count_2 (str,c):
    count = 0
    for i in range(len(str)):
        if str[i] == c:
            count += 1
    return count
#main part of program
str = input('enter the desired string\n')
print(Count_1(str, 'a'))
print(Count_2(str, 'a'))

### Exercise 5
### input variable is string type, so add the
### quotation marks before and after desired variable
### takes a character chain str and returns another chain
### with spaces inserted between the neighboring letters
def Spaces(str):
    return " ".join(str)

### ALTERNATIVE METHOD (NO .JOIN()
def Spaces2(str):
    NNstr = ""
    for i in range(len(str)):
        if str[i] != " ":
            NNstr = NNstr + str[i] + " "
    NNstr = NNstr.strip()
    return NNstr

### Exercise 6
### input variable is string type, so add the
### quotation marks before and after desired variable
### takes a character chain str and returns another coded chain.
### The code iscalculated by taking each pair of consecutive
### letters and changing the order in the pair
def code(str):
    nStr = ''
    for i in range (0, len(str),2):
        #Error control, if odd number of letters retain last letter as is
        if i + 1 == len(str):
            nStr += str[i]
        else:
            nStr += str[i+1] + str[i]
    return nStr
