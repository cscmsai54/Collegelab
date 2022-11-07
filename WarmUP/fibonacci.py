
print("enter the number of elements needed")
n=int(input())
first=0
second=1
if(n==1):
    print(first)
elif(n==2):
    print(first)
    print(second)
else:
    for i in range(n):
        if(i==1):
            print(first)
        elif(n==2):
            print(second)
        else:
            temp=first+second
            print(temp)
            first=second
            second=temp

    





































