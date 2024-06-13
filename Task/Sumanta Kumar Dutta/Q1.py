#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Function to arrange the strings in alphabetical order
def alpha(a):
    st = ""
    for i in range(97,123):
        for j in a:
            if(j == chr(i)):
                st = st + j
    return st

s = input("Enter the string s: ")
t = input("Enter the string t: ")
flag = False

if(1<=len(s) and 1<=len(t) and len(s)<=(5*104) and len(t)<=(5*104) and s.isalpha()==True and s.islower()==True and t.isalpha()==True and t.islower()==True):
    if(len(s)!=len(t)):
        flag = False
    else:
        if(alpha(s)==alpha(t)):
            flag = True
    print(flag)
else:
    print("Invalid input")
