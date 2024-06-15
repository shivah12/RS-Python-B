def count_character_frequency(input_str):
    frequency = {}

    for char in input_str:
        if char != ' ':
            frequency[char] = frequency.get(char, 0) + 1

    for char in sorted(frequency.keys(), key=lambda x: (x.lower(), x)):
        print(f"{char}-> {frequency[char]}")

count_character_frequency()
