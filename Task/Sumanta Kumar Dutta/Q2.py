#Suppose you are given a string containing only English alphabets (Uppercase and Lowercase letter both). You have to display the frequency of each character in lexicographical order.

st = input("Enter a string: ")
chk = "" #Stores all the checked characters

#Uppercase
for i in range(65,91):
    for j in st:
        if(j == chr(i)):
            if(chk.find(j)==-1):
                print(j+"-> "+str(st.count(j)))
                chk = chk + j
                
#Lowercase
for i in range(97,123):
    for j in st:
        if(j == chr(i)):
            if(chk.find(j)==-1):
                print(j+"-> "+str(st.count(j)))
                chk = chk + j
