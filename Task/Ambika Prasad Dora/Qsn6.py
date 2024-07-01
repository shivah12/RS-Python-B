n=int(input("Enter the number of elements : "))
A=[]
min=0
max=0
for i in range(n):
  c=int(input("Enter the element : "))
  A.append(c)

Z=sorted(A)
for i in range(n):
  if isprime(Z[i]):
   min=Z[i]
   break
for i in range(n-1,0,-1):

  if isprime(Z[i]):
    max=Z[i]
if max==min and max!=0 and min!=0:
  print("Difference = ",(max-min))
else:
  print("Difference = ",min)
if max==min and max==0:
  print(1)
