num=(input("Enter an integer: "))
a=[]
for i in num:
    a.append(i)
print("The input list is ", a)
b=0
for i in a:
    b=(b*10)+int(i)
c=b+1
d=[]
for i in str(c):
    d.append(i)
print("The final list is ", d)