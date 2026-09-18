# Print the Fibonacci series up to the required number of terms.

def fibonacci(n): 
   a ,b = 0,1
   print("Fibonacci Series: ",end=" ")
   for i in range(n):
       print(a,end=" ")
       c = a+b
       a = b
       b = c
fibonacci(8)
