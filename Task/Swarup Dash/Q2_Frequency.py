def char_frequency(s):
    frequency = {}
    
    uppercase_letters = []
    lowercase_letters = []
    
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            if char.isupper():
                uppercase_letters.append(char)
            else:
                lowercase_letters.append(char)
    
    all_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + \
                  [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    
    for char in all_letters:
        if char in frequency:
            print(f"{char}: {frequency[char]}")


#Example:
s = "Robotics Society"
char_frequency(s)
