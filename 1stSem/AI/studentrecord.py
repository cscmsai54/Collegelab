import pandas as pd
data = {
    "RollNumber" : [121,122,123,124],
    "Name" : ["student1","student2", "student3", "student4" ],
    "subject-1" : [80,70,76,54],
    "subject-2" : [99,69,55,88],
    "subject-3" : [66,77,55,67],
    "subject-4" : [78,90,100,78],
    "subject-5" : [56,99,67,45]
}
df = pd.DataFrame( data )
#print ("DataFrame : \n " ,df)  
p = df.idxmax(numeric_only=True)
#print(p[1])
print(df.index)
