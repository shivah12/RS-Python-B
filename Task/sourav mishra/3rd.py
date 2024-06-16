def one(digit:list[int]):
    for i in range(len(digit) -1,-1,-1):
        digit[i]+=1
    if    digit[i]<10:
        return digit
    if digit[i]==10:
        digit.insert(0,1)
    return digit

digit = [1,2,4]
print(one(digit))