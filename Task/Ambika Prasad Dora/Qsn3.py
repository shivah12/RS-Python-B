num=input("Enter a number : ")
l= len(num)
inputarr=[]
outputarr=[]
for i in num :
  inputarr.append(int(i))
print(f"Original= {inputarr}")
num1=int(num)
num1=num1+1
num1=str(num1)
for i in num1 :
  outputarr.append(int(i))
print(f"Incremented= {outputarr}")
