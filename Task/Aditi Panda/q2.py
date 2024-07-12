def count_characters(s):
    # Dictionary to store the frequency of each character
    frequency = {}

    # Count the frequency of each character
    for char in s:
        if char.isalpha():  # Consider only alphabetic characters
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    # Separate and sort the uppercase and lowercase characters
    uppercase_chars = sorted([char for char in frequency if char.isupper()])
    lowercase_chars = sorted([char for char in frequency if char.islower()])

    # Display the frequencies in the desired order
    print("Character frequencies in lexicographical order:")
    # Print uppercase characters first
    for char in uppercase_chars:
        print(f"{char}: {frequency[char]}")
    
    # Print lowercase characters next
    for char in lowercase_chars:
        print(f"{char}: {frequency[char]}")

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    count_characters(input_string)