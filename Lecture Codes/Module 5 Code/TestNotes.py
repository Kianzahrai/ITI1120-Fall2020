def TestNotes():
    flag = True
    marks = []

    while flag:
        valid = False
        while not valid:
            note = float(input("Enter a mark: "))
            valid = note_valid(note)

        marks.append(note)

        response = str(input("Do you want to continue (yes/no): "))
        if(response != "yes"):
          flag = False

    displayMarks(marks)
    print()
    print("The average mark is: ", averageNarks(marks))
    print("The highest mark is: ", maxMarks(marks))
    print("The lowest mark is: ", minMarks(marks))
        

def note_valid(nb):
    if(nb < 0 or nb > 100):
        print("the mark is invalid")
        return False
    print("the mark is valid")
    return True

def averageNarks(mat):
    sum = 0
    for index in range(0,len(mat)):
        sum = sum + mat[index]                    
    return sum/len(mat)

def maxMarks(mat):
    max = mat[0]
    for index in range(1,len(mat)):
        if mat[index] > max:
            max = mat[index]
    return max

def minMarks(mat):
    min = mat[0]
    for index in range(1,len(mat)):
        if mat[index] < min:
            min = mat[index]
    return min

def displayMarks(mat):
    print(len(mat), " marks have been entered")
    for index in range(0,len(mat)):
        print(mat[index], end=' ')




    


                
