def test2_Q3_try(s, p)
     if p in s:
          w = s.split(p)
          char = 1
          new_string = ''
          for i in range(len(w)):
               if i == (len(w)-1):
                    string1 = w[i]
                    new_string += string1
               else:
                    string1 = w[i] + '*' * char + 
                    new_string += string1
                    char += 1
               return new_string

     else:
          return s
