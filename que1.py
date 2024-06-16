def frequency(s):
    s=s.replace(" ","")
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char]=1
    sorted_chars = sorted(freq.keys())
    for char in sorted_chars:
        print(f"{char}-> {freq[char]}")
str=input("String is:")
frequency(str)