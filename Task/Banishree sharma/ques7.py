primefactor=[]
mrp=int(input("Enter An Amount:-"))

for i in range (2,mrp+1):
  if mrp%i==0:
    f=0
    for j in range(2,i):
      if i%j==0:
        f=1
        break
    if f==0:
      primefactor.append(i)

print(primefactor)
a=primefactor[0]
alfi=a
roy=mrp-a
print(alfi)
print(roy)