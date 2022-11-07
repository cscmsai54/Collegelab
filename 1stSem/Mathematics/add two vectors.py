import numpy as np
vectorlist1 = []
vectorlist2 = []
print("Enter Elements of Vector 1 : ")
for i in range(3):
    j = int(input(">>"))
    vectorlist1.append(j) 
print("Enter Elements of Vector 2 : ")
for i in range(3):
    j = int(input(">>"))
    vectorlist2.append(j)
vector1 = np.array(vectorlist1)
vector2 = np.array(vectorlist2)
added = vector1 + vector2 
print(vector1 , " + " , vector2 , " = " , added)