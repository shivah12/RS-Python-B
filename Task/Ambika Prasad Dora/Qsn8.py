a=int(input("enter the no of element:"))
li1=[]
for i in range (0,a):
    ele=input("enter the element:")
    li1.append(ele)
print(li1)
key=[]
for i in range(0,a):
    ele=li1[i]
    key.append(ele)
print(key)
value=[]
for i in range(0,a):
    k=li1.count(li1[i])
    value.append(k)
d={i:j for (i,j) in zip(key,value)}
print("the dictionary of frequncies of letters is:",d)
