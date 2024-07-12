def plusOne(digits):
    # Start from the last digit and work backwards
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the digit is 9, set it to 0 and carry over to the next digit
        digits[i] = 0
    
    # If all the digits were 9, we need an extra place at the beginning
    return [1] + digits

# Test cases
print(plusOne([1, 4, 8]))  # Should output [1, 4, 9]
print(plusOne([3, 6, 9]))  # Should output [3, 7, 0]
print(plusOne([9, 9, 9]))  # Should output [1, 0, 0, 0]