def factorial(num):
    if num == 0 or num== 1:
        return 1
    else:
        var = 1
        for i in range(1,num):
            var = var  * num   #5 * 4 =20 * 3 =60 * 2 =120 *1 = 120
            num-= 1
    return var

number = int(input("Enter a Number : "))
print(factorial(number))

#Easier Method
# def factorials(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact*= i
#     return fact
# print(factorials(5))
