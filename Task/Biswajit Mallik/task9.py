import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
columns = ['S_length', 'S_width', 'P_length', 'P_width', 'class']
iris_df = pd.read_csv(url, header=None, names=columns)


iris_df.rename(columns={
    'S_length': 'sepal length',
    'S_width': 'sepal width',
    'P_length': 'petal length',
    'P_width': 'petal width'
}, inplace=True)


print("Renamed DataFrame:")
print(iris_df.head())

sum_sepal_length = iris_df['sepal length'].sum()
print("\nSum of all sepal lengths:", sum_sepal_length)
index_max_petal_length = iris_df['petal length'].idxmax()
index_min_petal_length = iris_df['petal length'].idxmin()
print("\nIndex of maximum petal length:", index_max_petal_length)
print("Index of minimum petal length:", index_min_petal_length)