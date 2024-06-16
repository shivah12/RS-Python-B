st1=input("Enter a word")
st2=input("Enter next word")
if len(st1)!=len(st2):
    print("Not Anagrams")
else:
    if sorted(st1)==sorted(st2):
        print("These words are Anagrams")
    else:
        print("They are not Anagrams")
