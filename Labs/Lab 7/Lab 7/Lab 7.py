### ITI1120
### Kian Zahrai
### Lab 7


### Example of an array (Upper right Triangle)
def computeUpperTriangle(m):
    ''' (list) -> list
    returns the sum of the upper triangle
    Precondition: m has only integers
    '''
    sum = 0
    R = 0
    while R < len(m):
        C = 0
        while C < len(m[R]):
            if R <= C:
                sum = sum + m[R][C]
            C = C + 1
        R = R + 1
    return sum 

# To Test:
# print(computeUpperTriangle([[1,2],[3,4]]))

### Exercise 1
#Takes matrix and switches rows and columns
def Transpose(A):

    width = len(A)
    length = len(A[0])
    #Initialize new transformed array
    A_t = []

    for i in range(length):
        #Put blank lists in each array position
        A_t.append([])

    for j in range(width):
        for k in range(length):
            #Adding value into appropriate position
            A_t[k].append(A[j][k])

    return A_t


### Exercise 2
def sum_matrixes(a,b):

    #Initialize new sum array
    sum_ = []

    for i in range(len(a)):
        #Put new list in each position
        sum_.append([])

    for j in range(len(a)):
        for k in range(len(a[0])):
            #Insert sum of two array's positions into appropriate array position
            sum_[j].append(a[j][k]+b[j][k])

    return sum_


### Exercise 3
def product_matrixes (a,b):
    #Initialize new product array
    product = []

    #The product of a matrix:
    #Let matrix a and b have i rows and j columns
    #The product is a matrix with the number of rows of a and columns of b
    #An entry in the matrix ie. product[0][0] must be equivalent to
    #(a[o][0]+b[0][0])+(a[o][1]+b[1][0])+...+(a[len(a[0])-1][0]+b[0][len(a[0])-1])
    if range(len(a[0])) == range(len(b)) and range(len(a)) == range(len(b[0])):
        for i in range(len(a)):
            #Inserting list with current number of entries initilized
            product.append([0 for val in range(len(a))])

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    product[i][j] = product[i][j]+(a[i][k]*b[k][j])
        return product
            
    else:
        print("Matrix Multiplication not possible")
        return
