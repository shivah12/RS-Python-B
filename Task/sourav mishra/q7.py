def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primefactor(n):
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
    return factors

def roy_pay(n):
    roy_pays = []
    for price in products:
        factors = primefactor(price)
        if factors:
            min_factor = min(factors)
            roy_pays.append(price - min_factor)
        else:
            roy_pays.append(price) 
    return roy_pays

products = [10, 15, 21, 29, 35]
print(roy_pay(products))

