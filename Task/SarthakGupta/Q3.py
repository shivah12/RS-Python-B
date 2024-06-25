import numpy as np

a = input("Enter number")
l = len(a)
a = np.array(list(a),dtype = 'int32')

i = l-1

if(a[i]+1 == 10):
    while(i>=0):
        if(a[i]+1 >= 10):
            a[i] = 0
            a[i-1] += 1
        i-=1
else:
    a[i] += 1
    i -= 1

print(a)


