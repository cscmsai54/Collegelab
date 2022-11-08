import numpy as np
vectorlist = []
print("Enter Elements of Vector : ")
for i in range(3):
    j = int(input(">>"))
    vectorlist.append(j) 
vector = np.array(vectorlist)
k = int(input("Enter Scalar value : "))
sproduct = k * vector 
print(vector , " X ", k , " = ", sproduct)








