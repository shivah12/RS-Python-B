digits = []
l = int(input("Enter the number of digits : "))
for i in range(0, l):
    ele = int(input("Enter the digit :"))
    digits.append(ele)
    
if digits[-1] < 9:
    digits[-1] += 1
    print(digits)
else:
    digits[-1] = 0
    print([1] + digits)