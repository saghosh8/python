# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return (k & 1) == 0  # Bitwise AND with 1 checks if the last bit is 0 (even)

k = 10

print(is_even(k))
