r = int(input("Enter the number of Rows of the matrix: "))
c = int(input("Enter the number of Columns of the matrix: "))

m1 = [[0]*c for _ in range(r)]
m2 = [[0]*r for _ in range(c)]

print("Enter the Elements of the matrix below:\n")
for i in range(r):
    for j in range(c):
        m1[i][j] = int(input("Enter the Element " + str(i) + ", " + str(j) + " : "))

for i in range(r):
    for j in range(c):
        m2[j][i] = m1[i][j]

print("The Transpose of the matrix is :\n")
for i in range(c):
    for j in range(r):
        print(m2[i][j], end=" ")
    print("\n")