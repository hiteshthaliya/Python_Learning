# ├── 01_print_single_star.py
# ├── 02_print_four_stars.py
# ├── 03_print_n_stars_same_line.py
# ├── 04_print_n_stars_different_lines.py

print("*")
print("****")  #or 
print("*"*4)

n = int(input("enter number: "))
for i in range(1,n+1):
    print("*",end=" ")


num = int(input("\nenter numebr: ")) 
i = 0   
while i<num:
    print("*")
    i+=1