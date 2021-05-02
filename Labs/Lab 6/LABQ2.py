def histo_n(x):
    f = set(x)
    #eliminating the duplicates
    dict={}
    for i in f:
        dict[i]=x.count(i)
        #finding the count for each variable in tuple
    return dict
if __name__== "__main__":
    t=(1,2,-3,3,4,-3,3)
    dictionary=histo_n(t)
    dictlist=[]
    for key, value in dictionary.items():
        t = [key,value]
        dictlist.append(t)
dictlist.sort()
#sorting the dictlist
print(dictlist)
