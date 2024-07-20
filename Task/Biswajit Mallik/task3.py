digit=[1,2,9]
if digit[-1]+1 == 10 :
    digit[-1]=1
    digit.append(0)
    
else:
    digit[-1] = digit[-1]+1
    
print(digit)
