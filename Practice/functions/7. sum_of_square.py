# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_square(n):
    total = 0
    for i in range(1, n):
        square = i ** 2
        print(f'Square of {i} = {square}')
        total += square
    return total
    

n = 5
print(f'Sum of Squares till n-1 is = {sum_of_square(n)}')
