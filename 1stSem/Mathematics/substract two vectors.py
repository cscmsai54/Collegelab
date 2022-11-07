import numpy as np
vectorlist1 = []
vectorlist2 = []
print("Enter Vector 1 : ")
for j in range(3):
    j = int(input(">> "))
    vectorlist1.append(j)
print("Enter Vector 2 : ")
for j in range(3):
    j = int(input(">> "))
    vectorlist2.append(j)
vector1 = np.array(vectorlist1)
vector2 = np.array(vectorlist2)
subbed = vector1 - vector2
print(vector1, " - ", vector2, " = ", subbed)