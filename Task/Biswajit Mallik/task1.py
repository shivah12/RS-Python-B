s="anagram"
t="nagaram"
count = 0

if len(s)!=len(t):
    print("false")

for i in s :
    if i in t :
        count += 1

if count!=len(s):
    print("False")
else :
    print("True")    