a=[]
b=[]
s=0
n=int(input("Enter the number of elements in your array: "))
for i in range(0,n):
    element=int(input("Enter the elements: "))
    a.append(element)
print ("The entered array is: ",a)
for i in range(0,n):
    s=s+(a[i]*pow(10,(n-1-i)))
print(s)  
p=s+1
temp=p
for i in range(0,n):
    x=int(p/(pow(10,(n-1-i))))
    p=p%((pow(10,(n-1-i))))
    b.append(x)
print("The final array is: ",b)   