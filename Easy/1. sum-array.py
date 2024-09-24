# Sum of All Elements in an Array
# Write a function that takes an array of integers as input and returns the sum of all the elements in the array.

# Example Input: [1, 2, 3, 4]
# Example Output: 10

def sum_of_array(nums):
    
    sum = 0

    for i in nums:
        sum += i
    return sum

nums = [1, 2, 3, 4]
print(sum_of_array(nums))