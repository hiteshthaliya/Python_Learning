###---------------- Armstrong number ---------#
#An Armstrong number is a number where the sum of each digit raised to the power of the total number of digits equals the original number.
n = int(input("enter number for checking:- "))
original_n = n
total_digit = len(str(n))
total =0
for digit in str(n):
    total += int(digit)**total_digit
if total==original_n:
    print("Armstrong number")    
else:
    print("Not an Armstrong number")


#--------armstron number between 1 to 1000-----------#
for num in range(1,1001):
    original = num
    total_digit = len(str(num))
    total = 0

    for digit in str(num):
        total +=int(digit)**total_digit

    if total == original:
        print(original)    
