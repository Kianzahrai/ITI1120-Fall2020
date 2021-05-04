def pattern_to_stars(s, p): # 10 points
     '''(str, str)->str

     Precondition: p is not an empty string and all letters are lower-case

     Given a string s and another string p the function returns a new string where
     the first occurrence of p in s is replaced with one star, the second occurence with two starts
     and so on. 
     
     You may assume that no two patterns p in s overlap in s. Example:
     p="aa" s="aaab" cannot happen since "aa" pattern in the first two positions
     overlaps with "aa" pattern in the next two positions in s

     You CANNOT use the replace method from str module.
     Using that method will result in receiving zero for this function.

     Hints:
     - slicing may be helpful in this question
     - it may be easier to solve this problem with a while loop
     
     >>> pattern_to_stars("trabsabtt", "ab")
     'tr*s**tt'
     >>> pattern_to_stars("today123is123nice123d", '123')
     'today*is**nice***d'
     >>> pattern_to_stars("1a2b3", '123')
     '1a2b3'
     >>> pattern_to_stars("chipchip", 'chip')
     '***'
     >>> pattern_to_stars('', 'chip')
     ''
     '''

     pass
     # YOUR CODE GOES HERE

p = p.lower()
for index in p
