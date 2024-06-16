import pandas as pd
data = pd.read_csv("Iris.csv")
data.head()

data.sample(10)

data.columns

#The first one is the number of rows and
# the other one is the number of columns.
data.shape

print(data)

sum_data = data["SepalLengthCm"].sum()
print("Sum:",sum_data)

min_data=data["SepalLengthCm"].min()
max_data=data["SepalLengthCm"].max()

print("Minimum:",min_data, "\nMaximum:", max_data)