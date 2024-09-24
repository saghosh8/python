def prime_nums(N):
    primes = []
    # Include 2 as the only even prime number
    if N >= 2:
        primes.append(2)
    # Check for odd numbers only
    for i in range(3, N + 1, 2):
        is_prime = True
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

# List all prime numbers till 100
prime_numbers = prime_nums(100)
print(prime_numbers)
