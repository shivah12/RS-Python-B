def min_prime_factor(num):

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i
    return num

def roy_payment(N, prices):
    for price in prices:
        min_factor = min_prime_factor(price)
        roy_payment = price - min_factor
        print(roy_payment)

N = int(input())
prices = [int(input()) for _ in range(N)]

roy_payment(N, prices)
