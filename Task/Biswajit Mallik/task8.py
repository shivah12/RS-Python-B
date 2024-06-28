def count_frequencies(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

example_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_frequencies(example_list)
print(result)  
