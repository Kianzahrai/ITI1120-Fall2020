print("Enter the number with spaces between columns.")
print("One row per line, and an empty line at the end.")
matrice = []
while True:
    line = input()
    if not line: break
    valeurs = line.split()
    rangee = [int(val) for val in valeurs]
    matrice.append(rangee)
# Rows do not have to be of the same size,
# unless it is a matrix.
