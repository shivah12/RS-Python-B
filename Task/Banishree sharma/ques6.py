def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

N = int(input("Enter the number of points in the array : "))
A = []
for i in range(0, N):
    ele = int(input("Enter the element : "))
    A.append(ele)

sp = 0
lp = 0
for i in A:
    if is_prime(i):
        if i < sp:
            sp = i
        if i > lp:
            lp = i

if sp is None or lp is None:
    print("1")
else:
    print(abs(lp - sp))