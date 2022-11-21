import pandas as pd

df = pd.read_csv("Chategorical df.csv")
print("Chategorical Dataset >>")
print(df)
df['Department'].replace(['CS', 'AI' , 'ML'],[0,1,2], inplace=True)
df["Address"].replace(['Malappuram', 'Kozhikode', 'Kottayam', 'Trissur', 'Kannur', 'Trivandrum'], [0,1,2,3,4,5], inplace=True)
print ("Numerical Dataset >>")
print (df)