def smallest_prime_factor(n):
    if n <= 1:
        return n
    for i in range(2, n + 1):
        if n % i == 0:
            return i
    return n

def amount_roy_pays(N, prices):
    results = []
    for price in prices:
        min_prime = smallest_prime_factor(price)
        roy_pays = price - min_prime
        results.append(roy_pays)
    return results


N = 2    
prices = [5, 10]      
print(amount_roy_pays(N, prices))