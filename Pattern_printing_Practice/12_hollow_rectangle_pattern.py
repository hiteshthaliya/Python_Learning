# A hollow rectangle pattern is similar to the hollow square,
#  but the number of rows and columns can be different.
# * * * * * * *
# *           *
# *           *
# * * * * * * *


row= int(input("enter number of rows: "))
column= int(input("enter number of columns: ")) 
for i in range(row):
    for j in range(column):
        if i==0 or i==row-1 or j==0 or j==column-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()            