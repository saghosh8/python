# 8. Give a single command that computes the sum from Question 7, 
# relying on Python’s comprehension syntax and the built-in sum function.

def sum_of_square(n):
    sum_of_square = sum(i ** 2 for i in range(1, n))
    return sum_of_square

n = 5
print(f'Sum of Squares till n-1 is = {sum_of_square(n)}')
