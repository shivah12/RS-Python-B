#Alfi asked Roy to go shopping with her. Witty Roy came up with a condition. He said, for each product of MRP (Maximum Retail Price) R, she'll have to pay a minimum 
# of all the prime factors of R and he himself will pay the rest of the amount. Without giving it a second thought Alfi agreed. Now they bought N number of products.
#You're to find how much money Roy had to pay for each product.

def isPrime(a):
    c = 0
    for i in range(1,a):
        if(a%i==0):
            c=c+1
    if(c==1):
        return True
    return False


N = int(input("Enter the number of products: "))

if(N<2):
    print("Invalid Input")
    exit()

R = []
for i in range(N):
    ip = int(input("Enter the MRPs: "))
    if(ip>1000000):
        print("Invalid Input")
        exit()
    R.append(ip)

for i in R:
    ap = 0
    for j in range(2,i+1):
        if(i%j==0 and isPrime(j)==True):
            ap = j
            break
    print(i-ap)
