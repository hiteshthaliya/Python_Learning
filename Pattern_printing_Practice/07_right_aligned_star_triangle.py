#### right angle star triangle 
#     *
#    **
#   ***
#  ****
# *****

n = int(input("enter number: "))
i = 1
while i<=n:
    # for space
    j = 1
    while j<=(n-i):
        print(" ",end="")
        j+=1
    # print star
    j = 1
    while j<=i:
        print("*",end="")
        j+=1
    print() 
    i+=1       