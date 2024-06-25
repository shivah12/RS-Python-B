def primeChecker(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num / 2) +1):
        if num % i == 0:
            return False
    return True

f  = open('Q7text.txt','r')
N = int (f.readline())
r = [0]*N# costs
rp = [0]*N #roys pay
for i in range(N):
    r[i] = int (f.readline())
f.close()

for i in range(N):
    for j in range(r[i]):
        if primeChecker(j) :
            if r[i] % j == 0:
                rp[i] = r[i]-j
                break
print(rp)
