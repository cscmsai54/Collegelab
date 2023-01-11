def countDigit(number):
    count = 0
    while number :
        count = count +1
        number = number/10
    

num = int(input("Enter the Number: \n>>"))
power = countDigit(num)
check = num
sum = 0

while check :    
    mod = check % 10
    check = check/10
    add = pow(mod, power)
    sum = sum + add
    