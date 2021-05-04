# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    '''
    sclean=''
    for ch in word:
        if ch not in '(){}%!.?:,\',\",-,_,0123456789\n\t\\':
            sclean=sclean+ch.lower()
    return sclean


def test_letters(w1, w2):
    '''(str,str, list of str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''
    
    letters1=list(w1)
    letters2=list(w2)
    letters1.sort()
    letters2.sort()
    return letters1==letters2

    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word() function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''

    l=s.split()
    l_clean=[]
    for word in l:
        l_clean.append(clean_word(word))

    l_no_dup=[]
    for word in l_clean:
        if word not in l_no_dup:
            l_no_dup.append(word)
    l_no_dup.sort()
    return l_no_dup

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    The function returns a list of anagrams of the given word in wordbook

    >>> word_anagrams("listen", wordbook)
    ['silent', 'enlist', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['care', 'acre']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''

    anag_list=[]
    for ref_word in wordbook:
        if test_letters(word, ref_word)  and ref_word!=word:
            anag_list.append(ref_word)
    return anag_list
        

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''
    anagcount=[]
    for word in l:
        wc=0
        for ref_word in wordbook:
            if test_letters(word, ref_word) and ref_word!=word:
                wc = wc + 1
        anagcount.append(wc)
    return anagcount


def count_anagrams_v2(l, wordbook):
    anagcount=[]
    for word in l:
        anagcount.append(len(word_anagrams(word, wordbook)) )
    return anagcount



def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns all the words in l that
    have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'race', 'ear']
    '''
    
    k_anag=[]
    for i in range(len(anagcount)):
        if anagcount[i]==k:
            k_anag.append(l[i])
    return k_anag

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns all the words in l with maximum number of anagrams
    (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['listen', 'item']
    '''
    
    return k_anagram(l, anagcount, max(anagcount))

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns all the words in with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''
    
    return k_anagram(l, anagcount, 0)
            



                
    
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

if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")
    maxanag=max_anagram(l,anagcount)
    print(maxanag)
    
    print("\nHere are their anagrams:")
    for word in maxanag:
        print("Anagrams of", word, "are:", word_anagrams(word, wordbook))

    print("\nHere are the words from your file that have no anagrams:")
    print(k_anagram(l, anagcount, 0))

    print("\nSay you are interested if there is a word in your file that has exactly k anagrams")
    k=int(input("Enter an integer for k: "))
    anagrams=k_anagram(l, anagcount, k)
    if len(anagrams)==0:
        print("There is no word in your file with exactly", k, "anagrams.")
    else:
        print("Here is a word (words) in your file with exactly", k, "anagrams:")
        print(anagrams)



elif choice=='2':
    letters=input("Enter the letters that you have, one after another with no space: ")
    while " " in letters:
        print("Error: You entered space(s).")
        letters=input("Enter the letters that you have, one after another with no space: ")
    choice2=input("Would you like help forming a word with \n1. all these letters\n2. all but one of these letters?\n")
    while not(choice2=='1' or choice2=='2'):
        print("You must choose 1 or 2. Please try again.")
        choice2=input("Would you like help forming a word with \n1. all these letters\n2. all but one of these letters?\n")
    if choice2=="1":
        anagrams=word_anagrams(letters,wordbook)
        if letters in wordbook:
            anagrams.append(letters)
        anagrams.sort()
        if len(anagrams)==0:
            print("There is no word comprised of exactly these letters.")
        else:
            print("Here are the words that are comprised of exactly these letters:")
            print(anagrams)
    elif choice2=="2":
        print("The letters you gave us are:", letters)
        print("Let's see what we can get if we ommit one of these letters.")
        for i in range(len(letters)):
            sub_letters=letters[:i]+letters[i+1:]
            print("Without the letter in position", i+1, "we have letters", sub_letters)
            anagrams=word_anagrams(sub_letters,wordbook)
            if sub_letters in wordbook:
                anagrams.append(sub_letters)
                anagrams.sort()
            if len(anagrams)==0:
                print("There is no word comprised of letters:", sub_letters)
            else:
                print("Here are the words that are comprised of letters:", sub_letters)
                print(anagrams)
                           
                      
else:
    print("Good bye")


