def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

a = [1,2,3,4,5]
prime=[]

for i in a:
    if is_prime(i):
        prime.append(i)

prime.sort()

print(prime)
print("The req output = ",prime[-1] - prime[0])