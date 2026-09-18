# Find the HCF (Highest Common Factor) of the given numbers. 
a = int(input("Enter Number a: "))
b = int(input("Enter Number b: "))
small = a
hcf = 1
if a<b:
    small = b
for i in range(1,small):
    if a%i==0 and b%i==0:
        hcf = i

print("HCF:",hcf)       