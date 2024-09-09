# check if the Number is prime

# Upper limit for prime numbers
limit = 10

# Iterate through each number from 2 to limit
for num in range(2, limit + 1):
    is_prime = True  # Assume the number is prime
    
    # Check divisibility from 2 up to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Not a prime number
            break
    
    # Print the number if it is prime
    if is_prime:
        print(num)


