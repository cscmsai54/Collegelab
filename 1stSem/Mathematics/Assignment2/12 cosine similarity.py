import numpy as np
import math
def det(elements):
    sum = 0    
    for element in elements:
        elesq = element * element
        sum = sum+elesq
    dete = math.sqrt(sum)
    return dete
vector_list1 = []
vector_list2 = []
print ("Enter The first vector :")
for i in range(3):
    j = int(input(">>"))
    vector_list1.append(j)
vector1 = np.array(vector_list1)
print(vector1)
print ("Enter The first vector :")
for i in range(3):
    j = int(input(">>"))
    vector_list2.append(j)
vector2 = np.array(vector_list2)
print(vector2)
dot = np.dot(vector1,vector2)
detvector1 = det(vector1)
detvector2 = det(vector2)
cos = (dot/(detvector1*detvector2))
angle = math.degrees(math.acos(cos))
print("The Cosine Similarity(Angle) Between The vectors IS :")
print(angle)