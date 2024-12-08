st = str(input("Enter the first string :"))
nd = str(input("Enter the second string :"))

if len(st) == len(nd):
    print(sorted(st) == sorted(nd))
else:
    print("False")