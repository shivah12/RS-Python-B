str1 = input("Enter a word ")
str2 = input("Enter another word ")

str1 = sorted(str1)
str2 = sorted(str2)

if(str1 == str2):
    print("The given words are anagram")
else:
    print("The given words are not  anagram")