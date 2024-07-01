#Given an array, A, of length N. Find the absolute difference between the smallest and largest prime number in array A.

def isPrime(a):
    c = 0
    for i in range(1,a):
        if(a%i==0):
            c=c+1
    if(c==1):
        return True
    return False

n = int(input("Enter the length of the array: "))
number = []

#Input
for i in range(n):
    number.append(int(input("Enter a number: ")))
#Displaying the inputs
print(n)
for i in number:
    print(i, end =" ")
print()

number.sort()
for i in number:
    if(isPrime(i)==True):
        s = i #Smallest prime number
        break

number.sort(reverse=True)
for i in number:
    if(isPrime(i)==True):
        l = i #Largest prime number
        break

diff = int(l)-s
print(diff)
