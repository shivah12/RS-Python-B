rows=int(input("Enter the number of rows in the matrix: "))
columns=int(input("Enter the number of columns in the matrix: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(columns):
        element=int(input("Enter the element: ")) 
        row.append(element)
    matrix.append(row)
print("\nOriginal Matrix: \n")
for i in range(rows):
    for j in range(columns):
         print(matrix[i][j], end=" ")
    print()    

Tmatrix=[[matrix[j][i] for j in range(rows)] for i in range(columns)]         
print("\nTransposed Matrix:")
for i in range(columns):
        for j in range(rows):
            print(Tmatrix[i][j], end=" ")
        print()