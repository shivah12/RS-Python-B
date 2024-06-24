def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def minimum_prime_factor(num):
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            return i

def money_to_pay(mrp):
    min_prime = minimum_prime_factor(mrp)
    return mrp - min_prime

# Input the number of products
N = int(input("Enter the number of products: "))

for _ in range(N):
    mrp = int(input("Enter the MRP of the product: "))
    amount_to_pay = money_to_pay(mrp)
    print("Roy has to pay:", amount_to_pay)