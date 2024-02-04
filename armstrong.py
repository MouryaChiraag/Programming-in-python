def armstrong(number):
    x = number 
    a = 0
    while number > 0:
        var = number%10
        temp = var **len(str(x))     #27  #153 =153%10 = var =3 ; temp = 3 ** 3 =27 ; number = 153 ; 15%10 =5 ; temp =27 + 125
        a+= temp 
        number =number//10
    if a == x:
        return f"{a} Is a Armstrong Number"
    else:
        return f"{a} Is Not a Armstrong Number"
    

b = int(input("Enter a Number : "))
print(armstrong(b))


        