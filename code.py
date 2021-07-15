from os import access
import pandas as pd 
import csv 

df = pd.read_csv("dwarf_stars1.csv")
print(df.head())
print(df.columns)
print(df.dtypes)
df = df.dropna()
print(df.dtypes)

df["Radius"] = 0.102763 * df ["Radius"]
df["Mass"] = df ["Mass"].apply(lambda x:x.replace("$","").replace(",","")).astype("float")
df["Mass"] = 0.000954588 * df["Mass"]

print(df.head())
print(df.columns)
#print(df.drop(["unnamed:0"],axis=1,inplace=True))
print(df.head())
print(df.reset_index(drop=True,inplace=True))
df.to_csv("unit_converted_stars.csv")