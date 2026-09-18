# . Print the cube of each number from 1 to n.
# -----using FOR LOOP -----
n = int(input("Enter number: "))
for i in range(1,n+1):
    cube = i**3
    print(cube,end=" ")

# -----using WHILE LOOP -----
num = int(input("\nEnter number: "))
i  =1
while i<=n:
    cube = i**3
    print(cube,end=" ")
    i+=1