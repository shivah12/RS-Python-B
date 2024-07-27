#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

n = int(input("Enter the number of digits: "))
number = []
no = ""
#Input
for i in range(n):
    a = int(input("Enter a digit: "))
    number.append(a)

#Fetching the number
for i in number:
    no = no + str(i)
num = int(no)

res = num + 1 #Resultant number

#Output
result = []
for i in str(res):
    result.append(int(i))

print(result)
