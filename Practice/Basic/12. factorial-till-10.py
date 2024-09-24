#Finding Factorial till 5

num = 5

for i in range(1, num+1):
    fact = 1  # Reset factorial for each number
    for j in range(1, i+1):  # Inner loop to calculate factorial
        fact *= j
    print(f"Factorial of {i} is {fact}")
