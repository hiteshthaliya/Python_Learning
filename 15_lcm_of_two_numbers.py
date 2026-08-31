# Find the LCM (Least Common Multiple) of the given numbers
a = int(input("Enter number: "))
b = int(input("Enter number: "))

start = max(a, b)

for i in range(start, a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break
print("LCM:", lcm)