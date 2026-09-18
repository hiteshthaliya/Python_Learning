#Print all numbers between a and b that are divisible by 7. 
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
num = a
for i in range(num,b):
     if i%7 == 0:
          print(i,end=" ")