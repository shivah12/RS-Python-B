def plusOne(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        digits[i] = 0
    return [1] + digits