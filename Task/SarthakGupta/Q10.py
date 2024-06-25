import numpy as np

r = int (input("Enter the rows of array"))
c = int (input("Enter the columns of array"))
a = np.zeros((r,c),dtype = 'int')

aT = np.zeros((c,r),dtype = 'int')

for i in range(r):
    for j in range(c):
        a[i][j] = int (input(f"Enter the element for row {r} and column {c} = "))

for i in range(r):
    for j in range(c):
        aT[j][i] = a[i][j]


print(aT)
