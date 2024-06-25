lower = int(input ("Please, Enter the Lowest Range Value: "))  
upper= int(input ("Please, Enter the Upper Range Value: "))  
  
lst=[]
print ("The Prime Numbers in the range are: ")  
for number in range (lower, upper + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            lst.append(number)

print(lst)

large_primeno=max(lst)
small_primeno=min(lst)

absolute_diff=large_primeno-small_primeno
print("The absolute diff between largest and smallest prime number is:",absolute_diff)