def is_prime(num):
    if num <= 1:
        return 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 1
    return True

def min_max_prime_difference(arr):
    smallest_prime = float('inf')
    largest_prime = float('-inf')
    
    for num in arr:
        if is_prime(num):
            smallest_prime = min(smallest_prime, num)
            largest_prime = max(largest_prime, num)
    
    if smallest_prime == float('inf') or largest_prime == float('-inf'):
        return -1 
    else:
        return abs(largest_prime - smallest_prime)

