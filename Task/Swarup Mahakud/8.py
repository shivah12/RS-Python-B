lst = []
n = int(input("Enter the length of the list: "))
for i in range(0, n):
    ele = int(input("Enter the element :"))
    lst.append(ele)
    
fdict = {}

for j in lst:
    if j not in fdict:
        fdict[j] = 1
    else:
        fdict[j] += 1
print(fdict)