# #  print decreasing order star pattern
# *****
# ****
# ***
# **
# *

#  USING FOR LOOP
num = int(input("enter num: "))    
for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print()    

# USING WHILE LOOP 
n = int(input("enter numebr: "))
i = n
while i>=1:
    j = 1
    while j<=i:
        print("*",end="")
        j+=1
    print()    
    i -=1
