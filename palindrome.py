def palindrome(number):
    x = number
    temp = 0
    while(number > 0):
        var = number % 10
        temp = temp*10 + var
        number = number // 10
    if x == temp:
        return f"{x} is a Palindrome"
    else:
        return f"{x} is Not a Palindrome"
    
num = int(input("Enter a Number : "))
print(palindrome(num))
    