a=int(input("enter the no of element:"))
li=[]
for i in range (0,a):
    ele=input("enter the element:")
    li.append(ele)
print(li)
key=[]
for i in range(0,a):
    ele=li[i]
    key.append(ele)
print(key)
value=[]
for i in range(0,a):
    k=li.count(li[i])
    value.append(k)
d={i:j for (i,j) in zip(key,value)}
print("the dictionary is:",d)