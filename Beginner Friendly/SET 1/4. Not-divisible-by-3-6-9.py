# Write a program to print number till N -> Number, 
# which are not divisible by 3, 6 or 9

number = int(input("Enter the Number: "))

for i in range(1, number+1):
    if (i % 3 != 0 and i % 6 != 0 and i % 9 != 0):
        print(i)
        continue
    