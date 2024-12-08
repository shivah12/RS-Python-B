word=str(input("enter a word"))
wordl=list(word)
set1=set(word)
for i in set1:
    count=0
    for j in wordl:
        if j==i:
            count+=1
    print(i," <- ",count)
input()

        

    

