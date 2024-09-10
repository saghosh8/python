# check if the Number is prime

# Input number
num = int(input("Enter a number: "))

# Step 1: Calculate factorial of the number manually
fact = 1
for i in range(1, num + 1):
    fact *= i

# Step 2: Create a list of factors of the factorial
factors = []
for i in range(1, num + 1):
    if fact % i == 0:
        factors.append(i)

# Step 3: Check if the number is prime
if factors == [1, num]:
    print(f"Yes, {num} is a prime number!")
else:
    print(f"Sorry, {num} is not a prime number.")
