# Check for Duplicates in an Array
# Write a function that checks if a given array contains any duplicates.

# Example Input: [1, 2, 3, 4, 2]
# Example Output: True

def contains_duplicates(nums):
   if len(nums) != len(set(nums)):
       return True
   else:
        return False
    

nums = [1, 2, 3, 4, 2]
print(contains_duplicates(nums))