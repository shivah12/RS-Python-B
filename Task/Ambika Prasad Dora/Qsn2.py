string = "technology"
x=list(string)
y=sorted(x)
freq = {}
 
for i in y:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Number of all characters is\n " + str(freq))
