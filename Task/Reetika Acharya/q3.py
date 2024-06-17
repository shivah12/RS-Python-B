# -*- coding: utf-8 -*-
"""Q3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sadMtX96lpZC9uzNofbnj6moykdE6JYa

Problem 3: To increment a large integer represented as an array of digits, we can process the array from the end to handle the carry.
"""

def increment_number(digits):

    reversed_digits = digits[::-1]

    length = len(reversed_digits)
    for i in range(length):
        if reversed_digits[i] < 9:
            reversed_digits[i] += 1
            break
        else:
            reversed_digits[i] = 0


    digits = reversed_digits[::-1]

    return digits


digits_input = [1, 4, 3, 1, 9]
print(increment_number(digits_input))