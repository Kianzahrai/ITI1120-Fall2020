    # split splits the string using ' ' character as default delimiter
    s = cleaned_word.lower()
    uncleaned_word_list = s.split()

    # cleaned_word_list to extract the valid words alone and it ignores special characters
    cleaned_word_list = []
    # iterating the uncleaned_word_list
    for i in uncleaned_word_list:
        # if words as a whole contains only letters it is added to cleaned_word_list
        # isalpha checks if the word contains only letters
        if clean_word(i) not in cleaned_word_list:
            cleaned_word_list.append(clean_word(i))
        # else part if word consists special characters or numbers
        else:
            # temp_clean word to filter the string excluding numbers and special characters
            temp_clean = ""
            # iterating through each word
            for x in i:
                # if the character is a letter it is concatenated to temporary string temp_clean
                if x.isalpha():
                    temp_clean += x
            # the filtered clean word is then appended to cleaned_word_list
            cleaned_word_list.append(temp_clean)

    # iterated words is to keep track of the iterated words so if duplication doesn't occur
    iterated_words = []
    # clean_noduplicates_words to extract word list without any duplicates
    clean_noduplicates_words = []
    # iterating the cleaned_word_list
    for j in cleaned_word_list:
        # if j is not in the iterated_words it is appended to clean_noduplicates_words
        if j not in iterated_words:
            clean_noduplicates_words.append(j)
        # iterated_words stores all the searched words
        iterated_words.append(j)

    # sort() is used to sort the list
    clean_noduplicates_words.sort()

    # clean_sorted_noduplicates_words uses list comprehension to append the words from clean_noduplicates_words
    clean_sorted_noduplicates_words = [i for i in clean_noduplicates_words]
    print("The string is : \n" + s + "\nThe word list after create_clean_sorted_noduplicates_list() function :")
    print(clean_sorted_noduplicates_words)
    print("\n")

# function call
create_clean_sorted_noduplicates_list('able cat crea@te boat "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat.\n')
create_clean_sorted_noduplicates_list('Across Europe, infection rates are rising, With Russia reporting a record 24,423 daily '
                                      'cases on Wednesday and further 439 deaths')


