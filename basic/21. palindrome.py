#Find if the number is palindrome or not

# Input number
num = int(input("Enter a number: "))

# Convert the number to a string to easily reverse it
num_str = str(num)

# Check if the string representation is equal to its reverse
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
