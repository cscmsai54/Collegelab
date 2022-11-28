import numpy as np
vector_list = []
print ("Enter The elements of the vector : " )
for i in range (3):
    j = int(input(">> "))
    vector_list.append(j)
vector = np.array(vector_list)
maxnorm  = vector.flat[abs(vector).argmax()]
print(f"Max Norm Of {vector} = {abs(maxnorm)}"  )