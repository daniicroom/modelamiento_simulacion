import numpy as np
import panda as pd


myDataFrame = { "names": ["juan", "camilo", "jose"], "lastName": ["lopez", "zapata", "marinez"]}

df = pd.DataFrame(myDataFrame)
print(df.head(1))

print(df.tail(1))

dc = pd.read_csv("titanic2.csv", sep=';')

print(df.head())