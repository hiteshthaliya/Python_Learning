#Find and print the sum of all factors of the given number
n = int(input("Enter number: "))
total = 0
print("Factors: ",end=" ")

for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        total +=i
print(f"\nsum of factors : {total}")