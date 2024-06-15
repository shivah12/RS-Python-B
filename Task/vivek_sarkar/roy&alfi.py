def minprime(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)

    return min(factors)
NL=[]
roy=[]
alfi=[]
N=int(input("enter no of products"))
for i in range(0,N):
    R=int(input("enter price"))
    NL.append(R)
for j in NL:
    a=minprime(j)
    roy.append(a)
    alfi.append(j-a)
royamt=sum(roy)
alfiamt=sum(alfi)
print("roy will pay $",royamt,"/-")
print("alfi will pay $",alfiamt,"/-")

    
    
    
