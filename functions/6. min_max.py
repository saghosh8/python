# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


def min_max(data):

    smallest = largest = data[0]  # Initialize both smallest and largest with the first element

    for num in data:  # Loop through each number in the sequence
        if num < smallest:  # If the current number is smaller than the smallest, update smallest
            smallest = num
        elif num > largest:  # If the current number is larger than the largest, update largest
            largest = num

    return (smallest, largest)  # Return the smallest and largest numbers as a tuple

data = [3, 1, 7, 5, 9, 2]
print(min_max(data))  # Outputs (1, 9)
