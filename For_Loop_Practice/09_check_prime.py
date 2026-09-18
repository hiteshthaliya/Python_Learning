# Check whether the given number is a prime number.
n = int(input("enter number : "))
if n<=1:
    print("not a prime number")
else:
    is_prime = True
    for i in range(2,n):
        if n%i==0:
           is_prime = False
           break

    if is_prime:
       print("Prime number") 
    else:
        print("Not prime number ")  