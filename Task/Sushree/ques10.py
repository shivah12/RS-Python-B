def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])

    transposed_matrix = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6]]

print(transpose(matrix1)) 
print(transpose(matrix2))  
