import pandas as pd
def minimum(elements):
    min = 99999
    for element in elements:
        if element < min:
            min = element
    
    return min

def maximum(elements):
    max = -99999
    for element in elements:
        if element > max :
            max = element
    
    return max 

def mean(elements):
    sum = 0
    for element in elements:
        sum = sum + element
    length = len(elements)
    mean = sum/length
    return mean
    
df = pd.read_csv("numeric dataset.csv")
print(df)
for column in df.columns:
    print (f'<<< In {column} >>>')
    print("Minimum >>" ,minimum(df[column]), "Maximum >>" ,maximum(df[column]), "Mean >>" ,mean(df[column]))