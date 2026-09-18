# # Calculate and print the factorial of a given number.

n = int(input("Enter number for factorial: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(f"{n}! = {fact}")