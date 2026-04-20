def is_anagram(s,t):
    if 1 <= len(s) <= 5 * 10**4 and 1 <= len(t) <= 5 * 10**4:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
s= "anagram"
t= "nagaram"
print(is_anagram(s,t))
s = "rat"
t = "car"
print(is_anagram(s,t))