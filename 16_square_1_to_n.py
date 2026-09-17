# Print the square of each number from 1 to n.
#------ for loop -----
n = int(input("Enter number: "))
for i in range(1,n+1):
    square = i**2
    print(square,end=" ")

#-----While loop--------

a = int(input("\nEnter number: ")) 
i =1
while i<=n:
    square = i**2
    print(square,end=" ")
    i+=1