def is_prime(n):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_difference(arr):
    
    primes = [num for num in arr if is_prime(num)]
    
    if not primes:
        return 0  # Return 0 if there are no prime numbers in the array
    
    smallest_prime = min(primes)
    largest_prime = max(primes)
    
    return abs(largest_prime - smallest_prime)

A = [3,9 ,11,8,43,33,22]
print(find_prime_difference(A))
