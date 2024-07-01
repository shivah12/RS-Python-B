#Develop a Python program to count the frequency of each element in a list and return it as a dictionary.

n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    l.append(input("Enter an element: "))

d = {}
chk = []

for i in l:
    if(chk.count(i)==0):
        d[i] = l.count(i)
        chk.append(i)
    
print(d)
