str1=input("Enter string")
str2=input("Enter string")
if len(str1)!=len(str2):
    print("Not Anagrams")
else:
    if sorted(str1)==sorted(str2):
        print("true")
    else:
        print("false")
