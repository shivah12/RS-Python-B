st = input("Enter input ")
st = "".join(sorted(st))
l = len(st)
i = 0
count = 0

while i < l:
    c = st[i]
    if(c == 32):
        i+=1
        continue
    count = 1
    while i+1 < l and st[i+1] == c:
        count += 1
        i+=1
    print(f"{c} ==> {count}")
    i+=1



