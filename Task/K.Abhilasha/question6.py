def is_prime(n):
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

def min_max_prime_difference(A):
    min_prime = float('inf')
    max_prime = float('-inf')
    
    for num in A:
        if is_prime(num):
            min_prime = min(min_prime, num)
            max_prime = max(max_prime, num)
    
    if min_prime == float('inf') or max_prime == float('-inf'):
        return "No prime numbers found in the array"
    
    return abs(max_prime - min_prime)


A = [4, 6, 7, 10, 13, 15, 17]
print(min_max_prime_difference(A))