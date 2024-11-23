# Define a function called linearSearch that takes an array and a target value as input.
def linearSearch(array, target):  
    # Loop through each index in the array using its length.
    for index in range(len(array)):  
        # Check if the current element in the array matches the target value.
        if (array[index] == target):  
            # If a match is found, return the current index.
            return index  
    # If the loop completes without finding the target, return -1 to indicate not found.
    return -1  

# Create an array of elements to search in.
array = [10, 20, 30, 40, 50]  

# Set the target value to be searched in the array.
target = 3  

# Call the linearSearch function with the array and target, and print the result.
print(linearSearch(array, target))  
# Output will be -1 because 3 is not present in the array.
