def reverse(number):  
    temp =0      #1234%10 =123 ; temp= 0 *10 +4 = 4[save remainder in x] ; 1234//10 = 123%10 = 40+3
    for i in range(len(str(number))):
        var = number%10
        temp = temp * 10 + var
        number = number//10
    return temp

number = int(input("Enter a Number : "))
print(reverse(number)) 

# def reverse(number):  
#     temp =0      #1234%10 =123 ; temp= 0 *10 +4 = 4[save remainder in x] ; 1234//10 = 123%10 = 40+3
#     while(number>0):
#         var = number%10
#         temp = temp * 10 + var
#         number = number//10
#     return temp

# number = int(input("Enter a Number : "))
# print(reverse(number)) 

#BOTH ARE CORRECT
