import math

def countDigit(number):
    count = 0
    while number :
        count = count +1
        number = number//10
    return count

num = int(input("Enter the Number: \n>>"))
power = countDigit(num)
check = num
sum = 0

while check :    
    mod = check % 10
    check = check//10
    add = math.pow(mod, power)
    sum = sum + add

if num == sum :
    print(f"\n Your number {num} Is Armstrong.....")
else :
    print(f"\n Your number {num} Is NOT AN Armstrong.....")    