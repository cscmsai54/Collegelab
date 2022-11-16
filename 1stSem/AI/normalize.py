import pandas as pd
from sklearn import preprocessing
df = pd.read_csv("numeric dataset.csv")
print(df)

#normalized_df = ((df - df.mean()) / df.std)
normalized_df= preprocessing.MinMaxScaler()

print(normalized_df)

