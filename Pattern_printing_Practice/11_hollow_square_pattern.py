# A hollow square pattern is a square made of stars *,
#  but only the boundary/outer edges contain stars. 
# The inside is empty.

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n = int(input("enter number: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")    
              
    print()