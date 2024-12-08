def count_frequency(arr):
    frequency_dict = {}
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict

arr = [1, 2, 3, 4, 2, 3, 1, 2, 4, 5, "robotics"]
frequency = count_frequency(arr)
print(frequency)