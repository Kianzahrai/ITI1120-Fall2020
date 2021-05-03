def sum_matrixes(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return None
    result = []
    for i in range(len(matrix1)):
        lst = []
        if len(matrix1[i]) != len(matrix2[i]):
            return None
        for j in range(len(matrix1[0])):
            lst.append(matrix1[i][j] + matrix2[i][j])
        result.append(lst)
    return result

def main():
    m1 = eval(input("Enter first matrix: "))
    m2 = eval(input("Enter second matrix: "))
    print("Sum is " + str(sum_matrixes(m1, m2)))


main()
