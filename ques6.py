def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_difference(N, A):
    primes = []
    for i in range(N):
        if is_prime(A[i]):
            primes.append(A[i])

    if len(primes) == 0:
        return 1

    smallest_prime = min(primes)
    largest_prime = max(primes)
    return largest_prime - smallest_prime

A = [1, 2, 3, 4, 5, 6]       
N = 6    
print(prime_difference(N, A))