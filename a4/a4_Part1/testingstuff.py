def create_clean_sorted_nodupicates_list(s):
    s = s.lower()
    specialchar = '''!.?:,'"-_\()[]{}%1234567890\n\t''' # letters to check specials and numbers
    new_s = ""
    
    # remove special characters and numbers
    for char in s:
        if char not in specialchar:
            new_s = new_s + char
    
    # convert string into list using split()
    list2 = new_s.split(' ')
    
    output = [] # make empty list
    [output.append(z) for z in list2 if z not in output] # remove duplicates by using new list having single value
    
    print(sorted(output)) # print sorted list with no duplicates



    wordbook = open("english_wordbook.txt")
anagramWords = word_anagrams('listen',wordbook)
print(anagramWords)
