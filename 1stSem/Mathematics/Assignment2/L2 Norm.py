import numpy as np
vectorlist = []
print("Enter The Vector : ")
for i in range(3):
    j = int (input(">> "))
    vectorlist.append(j)
vector = np.array(vectorlist)
l2norm = np.linalg.norm(vector)
print("L2 Norm Of ", vector , " = ", l2norm)