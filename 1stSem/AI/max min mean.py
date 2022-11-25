import pandas as pd
def minimum():
    
    
    return min

def maximum():
    
    
    return max 

def mean():
    
    
    
    return mean
    
df = pd.read_csv("numeric dataset.csv")
print(df)
for column in df.columns:
    print("\n>>>Minimum<<<\n" ,minimum(df[column]))
    print("\n>>>Maximum<<<\n" ,maximum(df[column]))
    print("\n>>>Mean<<<\n" ,mean(df[column]))