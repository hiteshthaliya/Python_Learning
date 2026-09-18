# Print all factors of the given number. 
n = int(input("enter number: "))
count = 0
for i in range(1,n+1,):
    if n%i==0:
        print(i,end=" ")
        count +=1
print("\nTotal factors :",count)    