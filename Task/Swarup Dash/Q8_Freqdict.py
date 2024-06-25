def count_frequency(lst):
    
    frequency_dict = {}
    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict


sample_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4]
frequency_dict = count_frequency(sample_list)
print(frequency_dict)
