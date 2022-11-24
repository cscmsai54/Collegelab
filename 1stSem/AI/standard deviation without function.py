import pandas as pd
import math
df = pd.read_csv("numeric dataset.csv")
print("\n Dataframe :\n" )
print(df)
def standardDeviation(elements):
    sum=0
    for element in elements:
        sum = sum+element
    no = len(elements)
    avg = sum / no
    sumdiffsq = 0
    for element in elements:
        diff = element - avg
        sumdiffsq = sumdiffsq + (diff*diff)
    middev = sumdiffsq/(no-1)
    return math.sqrt(middev)
columns = df.columns
print("\nStandard Deviations Are :\n" )
for column in columns:
    if column == 'id' :
        continue
    else :
        print( standardDeviation(df[column]))

    
