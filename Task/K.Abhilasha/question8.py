strng=input("Enter elements of the list: ")
strg=strng.replace(" ","")
lst=[]
for i in strg:
    lst.append(i)
b=set()
for i in lst:
    b.add(i)
c=[]
d={}
for j in b:
    c.append(j)
for i in c:
    count=0
    for j in strg:
        if(i==j):
         count=count+1
        else:
            continue
    print(i, "---", count)
    d.update({i:count})
print(d)