import numpy as np
def acceptvector():
    vector_list = []
    for i in range(3):
        j = int(input(">>"))
        vector_list.append(j)
    vector = np.array(vector_list)
    return vector
while True :
    print("\n\n>>>CHECK<<<\n1) Assosciativity Of Addition\n2) Commutativity Of Addition\n3) Identity Element Of Addition\n4) Inverse Element Of Addition\n5) Distributrivity Of Scalar Multiplication Over Vector Addition \n6) Distributrivity Of Scalar Multiplication Over a Field Addition \n7) Compatibility Of Scalar Multiplication With Field Multiplication\n8) Identity Element Of Scalar Multiplication \n\n9) EXIT<<")
    choice = int(input("Choice >>:"))
    if choice == 1 :
        print("Enter Vector U :")
        vector1 = acceptvector()
        print("Enter Vector V :")
        vector2 = acceptvector()
        print("Enter Vector W :")
        vector3 = acceptvector()
        lhs = vector1 + (vector2 + vector3)
        rhs = (vector1 + vector2) + vector3
        print(f'U + (V+W) = {lhs} = (U+V) +W  = {rhs} ,\n\nHence Proven\n')
        input("<---Press Enter to continue--->")
        

















