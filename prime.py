def prime_num(n) :
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
    else:    
        return True

x = int(input("Enter a Number : "))
if prime_num(x):
    print("Prime Number")
else:
    print("Not a Prime NUmber")