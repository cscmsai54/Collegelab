import numpy as np
def acceptvector():
    vector_list = []
    for i in range(3):
        j = int(input(">>"))
        vector_list.append(j)
    vector = np.array(vector_list)
    return vector
while True :
    print("\n\n>>>CHECK<<<\n1) Assosciativity Of Addition\n2) Commutativity Of Addition\n3) Identity Element Of Addition\n4) Inverse Element Of Addition\n5) Distributrivity Of Scalar Multiplication Over Vector Addition \n6) Distributrivity Of Scalar Multiplication Over a Field Addition \n7) Compatibility Of Scalar Multiplication With Field Multiplication\n8) Identity Element Of Scalar Multiplication \n\n9) EXIT<<\n\n")
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
        print(f'\nU + ( V + W ) = {lhs} = ( U + V ) + W  = {rhs} ,\n\nHence Proven\n')
        b = input("<---Press Enter to continue--->")
    elif choice == 2 :
        print("Enter Vector U :")
        vector1 = acceptvector()
        print("Enter Vector V :")
        vector2 = acceptvector()
        lhs = vector1 + vector2
        rhs = vector2 + vector1
        print(f"\nU + V = {lhs} = V + U = {rhs} ,\n\nHence Proven\n")
        b = input("<---Press Enter to continue--->")
    elif choice == 3 :
        print("Enter Vector V :")
        vector1 =acceptvector()
        ans = vector1 + 0
        print(f"\nV + I = {ans} , \n\nHence Proven\n")
        input("<---Press Enter to continue--->")
    elif choice == 4 :
        print("Enter Vector V :")
        vector1 =acceptvector()
        ans = vector1 + (-vector1)
        print(f"\nV + (-V) = {ans} ,\n\nHence Proven\n")
        input("<---Press Enter to continue--->")
    elif choice == 5 :
        print("Enter Vector U :")
        vector1 = acceptvector()
        print("Enter Vector V :")
        vector2 = acceptvector()
        const = int(input("Enter Value For Constant (C)\n>>"))
        lhs = const * (vector1 + vector2)
        rhs = (const * vector1) + (const * vector2)
        print(f"\nC * ( U + V ) = {lhs} = C * U + C * V = {rhs} ,\n\nHence Proven\n")
        input("<---Press Enter to continue--->")
    elif choice == 6 :
        print("Enter Vector V :")
        vector1 = acceptvector()
        const1 = int(input("Enter Value For Constant (C)\n>>"))
        const2 = int(input("Enter Value For Constant (B)\n>>"))
        lhs = (const1 + const2) * vector1
        rhs = (const1 * vector1) + (const2 * vector1)
        print(f"\n( C + B ) * V = {lhs} = ( C * V ) + ( B * V ) = {rhs} ,\n\nHence Proven\n")
        input("<---Press Enter to continue--->")
    elif choice == 7 :
        print("Enter Vector V :")
        vector1 = acceptvector()
        const1 = int(input("Enter Value For Constant (C)\n>>"))
        const2 = int(input("Enter Value For Constant (B)\n>>"))
        lhs = const1 * (const2 * vector1)
        rhs = (const1 * const2) * vector1 
        print(f"\nC * ( B * V  ) = {lhs} = ( C * B ) * V = {rhs} ,\n\nHence Proven\n")
        input("<---Press Enter to continue--->")
    elif choice == 8 :
        print("Enter Vector V :")
        vector1 = acceptvector()
        ans = vector1 * 1
        print(f"\nV * I = {ans} = V ,\n\nHence Proven\n")
        input("<---Press Enter to continue--->")
    elif choice == 9 :
        print("Okey.Bye")
        exit()
    else :
        print("\nPlease Enter Any Valid Choice !!!!\n")
        input("<---Press Enter to continue--->")