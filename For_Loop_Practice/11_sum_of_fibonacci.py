# Find and print the sum of the Fibonacci series. 
n = int(input("enter: "))
a,b = 0,1
total = 0
for i in range(0,n):
    print(a,end=" ")
    total +=a
    c = a+b
    a = b
    b = c
print("\ntotal sum of given  fibonbacci series : ", total)    