def min_prime(p):
    for i in range(2, 1001):
        if p % i == 0:
            return i
    return n

n = int(input("Enter the number of products bought (n>=2) : "))
print()
for j in range(0,n):
    r = int(input("Enter the MRP of product " + str(j+1) + " : "))
    print("Rs " + str(r - min_prime(r)))