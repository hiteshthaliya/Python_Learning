##  A rectangle star pattern has:

# A fixed number of rows
# A fixed number of columns
# Every row contains the same number of stars

row = int(input("enter number of rows: "))
column = int(input("enter number of columns: "))
for  i in range(1,row+1):
    for j in range(1,column+1):
        print("*", end="")
    print()    