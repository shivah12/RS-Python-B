R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):		                      # A for loop for row entries
	a =[]
	for j in range(C):	                      # A for loop for column entries
		a.append(int(input()))
	matrix.append(a)


for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()

transpose = []
for j in range(C):
  transpose.append([])
  for i in range (R):
    t_num = matrix[i][j]
    transpose[j].append(t_num)

#printing the transpose matrix
print('Transpose matrix: ')
for i in range (R):
  for j in range (C):
    print (transpose[i][j], end = ' ')
  print()
