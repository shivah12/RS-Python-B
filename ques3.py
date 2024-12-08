def plus_one(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        digits[i] = 0

    return [1] + digits

example1 = [1, 2, 3]
example2 = [4, 3, 2, 1]
example3 = [9]

print(plus_one(example1))  
print(plus_one(example2))  
print(plus_one(example3)) 

