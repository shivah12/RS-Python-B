m=input("Enter a string:")
a="".join(m.split())
b=list(sorted(a))
D={}
for i in b:
    if i in D:
        D[i]+=1
    else:
        D[i]=1
for f in D:
    print(f,"->",D[f])