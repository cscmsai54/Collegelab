import pandas as pd
def normalize(elements):
    min = elements.min()
    max = elements.max()
    low = max - min 
    col = []
    for element in elements:
        upper = element - min
        norm = upper / low
        norm = round(norm ,3)
        col.append(norm)
    return col
df = pd.read_csv("numeric dataset.csv")
ndf = pd.DataFrame()
print("\nDataFrame :\n\n ", df)
for column in df.columns:
    normalized_df= normalize(df[column])
    ndf[column]=normalized_df
print("\n Normalized Data : \n\n" ,ndf)



