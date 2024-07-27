#Given a dataset IRIS (CSV file) (download it) and create a dataframe from it. Now change the attributes according to the following information:
#1- S_length to sepal length
#2- S_width to sepal width
#3- P length to petal length
#4-P_width to petal width

#-Now write a program to find the sum of all lengths of all sepal length in cm.
#Find the index value of maximum and minimum length from petal lengths.(Hint: you can use predefined functions idmax() and idmin())
#Note: Number of instances is 150

import pandas as pd

#sepal.length, sepal.width, petal.length, petal.width, variety
data = pd.read_csv('iris.csv') #Creating a dataframe from the iris.csv file
data.rename(columns={'sepal.length':'S_length', 'sepal.width':'S_width', 'petal.length':'P_length', 'petal.width':'P_width'}, inplace=True)

#Finding the sum of all sepal length in cm.
sum = 0.0
for i in range(150):
    s_length = float(data.at[i,'S_length'])
    sum = sum + s_length

print("The sum of all sepal lengths =",end=" ")
print(sum, end=" cm\n\n")

#Finding the index value of maximum and minimum length from petal lengths
print("The index value of maximum ",end=" ")
print(data[['P_length']].idxmax(), end="\n\n")
print("The index value of minimum ",end=" ")
print(data[['P_length']].idxmin())
