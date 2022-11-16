array = []
limit = int(input("Enter The Size of array :\n>> "))
for i in range(limit):
    a = int(input(f"Enter {(i+1)} th element\n>> "))
    array.append(a)
print (array)
print("\nsorted array\n")
array.sort()
print(array)
val = int(input("Enter The Value To be Searched :\n>> "))
first = 0
end = limit-1
mid = 0
flag = 0
while first <=  end:
    mid = (first+end)//2
    if array[mid] > val  :
        end = mid - 1
    elif array[mid] < val   :
        first = mid+1
    elif array[mid] == val:
        flag=1
        break
    else :
        flag = -1  
if flag == -1 :
    print("Value Not Found")
elif flag ==1 :
    print(f"Value Found At Position {mid+1}")