import operator
def Frequency(my_list):
    frequency = {}
    for items in my_list:
        if (items in frequency):
            frequency[items] += 1
        else:
            frequency[items] = 1
    for key, value in frequency.items():
        print("%d : %d" %(key,value))
           
        
my_list = [1,2,3,4,4,2,5,7,3,5,2,3,3,2,4,4,4,2,2,1,2]
print("Original List: ",my_list)
print("Frequency of each item: ",Frequency(my_list))

