def multiplicationTable(base, start, end):
    print('Fragment of the multiplication table by',base,':')
    i = start
    while i <= end:
        print(i, 'x', base, '=', i*base)
        i += 1


def muultiplicationTables(bases, start, end):

    for index in range(len(bases)):
        multiplicationTable(bases[index], start, end)
        print() 

def multiplicationTable2(bases, start, end):

    for index in range(len(bases)):
        multiplicationTable(bases[index], start[index], end[index])
        print() 


    


                
