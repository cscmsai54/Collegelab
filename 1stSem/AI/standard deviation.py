import pandas as pd
df = pd.read_csv("numeric dataset.csv")
print(df.to_string(), "\n")
print(df.std())