m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
matrix = []

for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element at ({i}, {j}): "))
        row.append(element)
    matrix.append(row)

print("Original Matrix:")
for row in matrix:
    print(row)

# Initialize the transpose matrix with zeroes
tmatrix = []
for i in range(n):
    row1 = [0] * m
    tmatrix.append(row1)

# Transpose the matrix
for i in range(m):
    for j in range(n):
        tmatrix[j][i] = matrix[i][j]

print("Transposed Matrix:")
for row in tmatrix:
    print(row)


input()
