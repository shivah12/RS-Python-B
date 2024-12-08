def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    char_count_s = {}
    char_count_t = {}
    
    for char in s:
        char_count_s[char] = char_count_s.get(char, 0) + 1
        
    for char in t:
        char_count_t[char] = char_count_t.get(char, 0) + 1
    
    return char_count_s == char_count_t

s1 = "anagram"
t1 = "nagaram"
print(is_anagram(s1, t1))  

s2 = "rat"
t2 = "car"
print(is_anagram(s2, t2)) 
