#Given a 2D integer array matrix, return the transpose of matrix.
#The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

if(m<1 or n>1000 or (m*n)>105 or (m*n)<1):
    print("Invalid input")
    exit()

#Creating the matrix
mat = []
for i in range(m):
    mat.append([])

#Initializing the matrix with 0s
for i in range(m):
    for j in range(n):
        mat[i].append(j)
        mat[i][j] = 0

#User input
print("Enter the elements:-")
for i in range(m):
    for j in range(n):
        ip = int(input("Element: "))
        if(ip<-109 or ip>109):
            print("Invalid input")
            exit()
        mat[i][j] = ip

#Creating the transpose matrix:-
trans = []
for i in range(n):
    trans.append([])

#Initializing the transpose matrix with 0s
for i in range(n):
    for j in range(m):
        trans[i].append(j)
        trans[i][j] = 0

#Finding transpose
for i in range(n):
    for j in range(m):
        trans[i][j] = mat[j][i]

print("Input matrix:", end=" ")
print(mat)
print("Output matrix:", end=" ")
print(trans)
