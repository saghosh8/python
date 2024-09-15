# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.



def is_multiple(n, m):  
    # Check if the remainder of n divided by m is zero
    return n % m == 0  

n = 10  # Assign value to n
m = 5   # Assign value to m

# Call the function and print the result
print(is_multiple(n, m))  # Outputs True since 10 is divisible by 5
