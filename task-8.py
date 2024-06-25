def count_frequencies(lst):
    frequency_dict = {}
    
    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    return frequency_dict

example = [1,2,2,3,5,6,4,7,7]
result = count_frequencies(example)
print(result)  