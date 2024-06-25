def is_anagram(s, t):
    
    if len(s) != len(t):
        return False  
    
    count_s = [0] * 26       #list of size 26 to store each 26 alphabet :)
    count_t = [0] * 26       #list of size 26 to store each 26 alphabet :)
    
    for char in s:
        index = ord(char) - ord('a')             #Ascii value of a=97
        count_s[index] += 1
    
    for char in t:
        index = ord(char) - ord('a')           
        count_t[index] += 1
    
    for i in range(26):
        if count_s[i] != count_t[i]:
            return False  
    return True  

#Example 1
s1 = "anagram"
t1 = "nagaram"
print(is_anagram(s1, t1))  

#Example 2
s2 = "rat"
t2 = "car"
print(is_anagram(s2, t2)) 

