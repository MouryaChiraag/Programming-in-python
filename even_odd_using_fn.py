def even_odd(n):
    if n%2 == 0:
        return True
    else:
        return False

number = int(input("Enter Your Number : "))
if even_odd(number):
    print("Even Number")
else:
    print("Odd Number")    

