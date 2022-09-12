import pandas as pd


df = pd.read_csv("datasets/dataset-salary/data-faculty.csv")

column1 = "Count"
column2 = "Faculty"


print(df[column1].describe())
print("Variance of column Count: ", df[column1].var())
print("Median of column Count: ", df[column1].median())

normalized_minmax=(df[column1]-df[column1].min())/(df[column1].max()-df[column1].min())

print("Normalized MIN-MAX: ")

print(normalized_minmax)

normalized_zscore = (df[column1] - df[column1].mean())/(df[column1].var())

print("Normalized Z-SCORE: ")

print(normalized_zscore)

correlation = df[[column1, column2]].corr()

print(correlation)
