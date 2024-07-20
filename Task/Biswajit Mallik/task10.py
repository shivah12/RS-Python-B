def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    
    transposed = [[0] * rows for i in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = matrix[r][c]
    
    return transposed

example_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = transpose_matrix(example_matrix)
print(result)
