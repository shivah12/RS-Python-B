
N=int(input("enter disired length of array"))
A=[0]*(N+1)
for i in range(1,N):
    A[i]=int(input("enter a number"))
primeset=set()
for j in A:
    count=0
    for k in range(1,j):
        if j%k==0 and j!=0:
            count+=1
    if count<=2:
        primeset.add(j)
largest=max(primeset)
smallest=min(primeset)
diff=largest-smallest
for m in A:
    print(m)
print("the difference between largest prime no and smallest prime no is: ",diff)
print(primeset)
    
          
          
