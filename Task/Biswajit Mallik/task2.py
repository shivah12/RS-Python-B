word = input("Enter your word:")
word = sorted(word)
print(word)
for i in word:
    if i.isalpha():
        print(i , "->" , word.count(i))

