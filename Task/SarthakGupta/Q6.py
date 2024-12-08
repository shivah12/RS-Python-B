import numpy as np
##You can make the changes in test1.txt to check the working of this program

def primeChecker(num):
    if num <= 1:
        return False

    for i in range(2,int(num / 2)+1):
        if num % i == 0:
            return False
    return True

f = open('test1.txt', 'r')  # Passing Reference of file in read mode
N = int(f.readline())  # Reading the first line
arr = np.array(f.readline().split(),dtype  = 'int32')  # Reading the second line and converting it to a numpy array
print(N)
print(arr)
f.close()
minP = 2147483647 #Assigning the minP variable with max int value will facilitate store the min value
maxP = -2147483648 # Vice versa

for n in arr:
    if primeChecker(n) :
        if n > maxP :
            maxP = n
        if  n < minP :
            minP = n
print(minP)
print(maxP)
print(f"The abs diff of max and min prime number in this array is   =   {abs(maxP - minP)}")

