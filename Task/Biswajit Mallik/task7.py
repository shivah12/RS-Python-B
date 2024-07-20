def min_prime_factor(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

def calculate_roy_payment(n, prices):
    result = []
    for price in prices:
        min_prime = min_prime_factor(price)
        roy_payment = price - min_prime
        result.append(roy_payment)
    return result

n = int(input("Enter the number of products: "))
prices = []
for _ in range(n):
    prices.append(int(input()))

payments = calculate_roy_payment(n, prices)

for payment in payments:
    print(payment)
