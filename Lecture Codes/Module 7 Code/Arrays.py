mat = [[1,2,3],[4,5,6],[7,8,9]]

for row in mat:
    print(row)
    
def display(mat):
    for row in mat:
        for col in row:
            print(col, end=" ")
    print()

def writing1():
    m = int(input("please enter the number of rows: "))
    n = int(input("Please enter the number of columns: "))

    mat = []
    for row in range(m):
        mat.append([]) # create an empty row
        for col in range(n):
            nb = int(input("mat["+str(row)+","+str(col) +"] ="))
            mat[row].append(nb) # fill up the row in question

        for row in mat:
            for col in row:
                print(col,end=" ")
            print()
                           
def writing2():
    m = int(input("Please enter the number of rows: "))
    mat = []

    for row in range(m):
        print("complete the row",row,"(integers seperated by spaces)")
        row = [int(val) for val in input().split()]
        mat.append(row) # a whole row

    for row in mat:
        for col in row:
            print(col, end = ' ')
        print()

# declare an empty matrix (m = []) before calling writing3(m):
mat = []
def writing3(mat):
    print("Please enter numbers with spaces between the columns.")
    print("One row per line, end with an empty line")

    while True:
        row = input()
        if not row:
            break

        nb = row.split()
        row = [int(nb) for nb in nb]
        mat.append(row)

    for row in mat:
        for col in row:
            print(col, end=" ")
        print()

def maxInMatrix(mat):
    max = mat[0][0]

    for row in range(1, len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] > max:
                max = mat[row][col]

    return max

def minInMatrix(mat):
    min = mat[0][0]

    for row in range(1, len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] < min:
                min = mat[row][col]

    return min

        
# A diagonal array must have 0s every where beside on the diagonal:
def checkDiag1(mat): # using a for loop:
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if (row != col and mat[row][col] != 0):
                return False
    return True

def checkDiag2(mat): # using a while loop:
    row = 0

    while row < len(mat):
        col = 0
        while col < len(mat[row]):
            if (row != col and mat[row][col] != 0):
                return False
            col = col + 1
        row = row + 1
    return True

def checkDiag3(mat):
    isDiagonal = True # Initialization to True
    row = 0

    while row < len(mat) and isDiagonal: #same as : and isDiagonal == True:
        col = 0
        while col < len(mat[row]) and isDiagonal: #same as : and isDiagonal == True:
            if (row != col and mat[row][col] != 0):
                isDiagonal = False
            col = col + 1
        row = row + 1
    return isDiagonal

# to remove a column (us the column index)
def eraseColMatrix(mat, col):
    for row in range(len(mat)):
        del(mat[row][col])

# to remove a row:
# del mat[row]

# to add a column after the last one:
def appendColumn(mat):
    for row in mat:
        val = int(input("Please enter a value: "))
        row.append(val)

# to add a row after the last one:
def appendRow(mat, row):
    mat.append(row)

    
# to add a row to a specific index:
def addRow(mat, index, row):
    mat.insert(index, row)

# to add a column at a specific index:
def addColumn(mat, index):
    for row in mat:
        val = int(input("Please enter a value: "))
        row.insert(index, val)

# Declare an empty matrix prior to calling this function: m = []
def transpose(mat):

    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

def build(mat, m, n):
    import random
    for row in range(m):
        mat.append([])
        for col in range(n):
            mat[row].append(random.randint(0,20))

def display(mat):
    for row in mat:
        for col in row:
            print(col, end=" ")
        print()

def rebuild(mat):
for row in range(len(mat)):
    col = row + 1
    while col < len(mat):
        if col != row:
            temp = mat[row][col]
            mat[row][col] = mat[col][row]
            mat[col][row] = temp
        col += 1

        
