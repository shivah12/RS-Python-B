
n = int(input("Enter number of elements in the list: "))


mylist = []


for i in range(n):
    a = str(input("Enter an element: "))
    mylist.append(a)


myset = set(mylist)

mydict = {}


for i in myset:
    count = 0
    for j in mylist:
        if j == i:
            count += 1
    mydict[i] = count
print(mydict)

input()
