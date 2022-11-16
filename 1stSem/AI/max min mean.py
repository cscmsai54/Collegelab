import pandas as pd
df = pd.read_csv("numeric dataset.csv")
print(df)
print("\n>>>Minimum<<<\n" ,df.min())
print("\n>>>Maximum<<<\n" ,df.max())
print("\n>>>Mean<<<\n" ,df.mean())