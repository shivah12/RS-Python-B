def frequency_in_lexicographical_order(s: str):
    frequency = {}
    for char in s:
        if char.isalpha():  
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    sorted_uppercase = sorted([char for char in frequency if char.isupper()])
    sorted_lowercase = sorted([char for char in frequency if char.islower()])

    for char in sorted_uppercase:
        print(f"{char}: {frequency[char]}")
        
    for char in sorted_lowercase:
        print(f"{char}: {frequency[char]}")

input_string = "Robotics Society"
frequency_in_lexicographical_order(input_string)
