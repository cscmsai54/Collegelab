print("\ngreatest among 3 numbers")
a=int(input("first number:"))
b=int(input("second number:"))
c=int(input("third number:"))
if(a>b):
    if(a>c):
        print("a is big")
    else:
        print("c is greater")
elif(b>a):
    if(b>c):
        print("b is big")
    else:
        print("c is big")
else:
    print("all are same") 
                        
