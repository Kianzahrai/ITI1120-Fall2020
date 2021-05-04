def get_list_ofint(s): # 5 points
     '''(str)->list of int
     Precondition: s string that looks like a sequence in integers where between
     every pair of consecutive integers we have 1 space of a comma and a space.

     More preconditions: s has at least one substring that looks like an integer
     
     Returns a list of integers from s
     
     >>> get_list_ofint("10 22, 7 0 -5, 1")
     [10, 22, 7, 0, -5, 1]
     >>> get_list_ofint("231, -5, 12")
     [231, -5, 12]
     >>> get_list_ofint("231 -5 -7")
     [231, -5, -7]
     >>> get_list_ofint("-7,")
     [-7]
     '''

     pass
     # YOUR CODE GOES HERE

    s = s.split()
    filtered = ","
    new_s = ""
    for char in s:
        if char not in filtered:
            new_s += char
    
    new_s = new_s.split()
    new_s2 = []
    for index in new_s:
        new_s2.append(int(index))
    return new_s2
