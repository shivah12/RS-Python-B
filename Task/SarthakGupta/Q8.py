str = input("Enter a string  : ")
str = list(str)
ele_dict = {}
str.sort()
count  = 0
for i in str:
    if i in ele_dict:
        ele_dict[i]+=1
    else:
        ele_dict[i] = 1
print(ele_dict)
