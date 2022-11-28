import numpy as np
vector_list = []

print ("Enter The elements of the vector : " )
for i in range (3):
    j = int(input(">> "))
    vector_list.append(j)

vector = np.array(vector_list)
l2norm = np.linalg.norm(vector)
squaredL2Norm = l2norm * l2norm

print(f"Squared l2 Norm Of {vector} = {squaredL2Norm}"  )