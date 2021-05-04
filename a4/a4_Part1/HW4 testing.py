def test_letters(w1, w2):
    a = sorted(w1)
    b = sorted(w2)
    if a == b:
        return True
    else:
        return False

def word_anagrams(word, wordbook):

    anagramWords = [] # to store the anagram words
    
    strings = [] # to store the words/strings present in the file in the list 
   
    words = wordbook.read().split()
    
    for string in words:
        isit = test_letters(string,word)
        if isit is True:
            anagramWords.append(word)
            
    wordbook.close()
    return sorted(anagramWords)


wordbook = open("english_wordbook.txt")
anagramWords = word_anagrams('listen',wordbook)
print(anagramWords)



##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

# when asking for k from the user you may assume that they will enter non-negative integer
if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")

    # YOUR CODE GOES HERE    
    
elif choice=='2':

    #YOUR CODE GOES HERE
    
    pass
                       
                      
else:
    print("Good bye")
