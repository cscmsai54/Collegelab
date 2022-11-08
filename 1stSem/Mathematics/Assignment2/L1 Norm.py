import numpy as np
vectorlist = []
print("Enter The Vector : ")
for i in range(3):
    j = int(input(">> "))
    vectorlist.append(j)
vector = np.array(vectorlist)
l1norm = np.linalg.norm(vector, 1)
print("L1 Norm Of ", vector , " = ", l1norm)