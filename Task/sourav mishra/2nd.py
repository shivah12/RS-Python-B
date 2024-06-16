def character_frequency(string):
    
    frequency = {}

   
    for char in string:
        if char.isalpha():  
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    
    sorted_frequency = dict(sorted(frequency.items()))

    
    for char, count in sorted_frequency.items():
        print(f"{char}: {count}")

input_str = "Car is busted"
character_frequency(input_str)