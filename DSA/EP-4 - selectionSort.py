# Define the selectionSort function that takes an array as input
def selectionSort(array):  
    # Get the length of the array
    n = len(array)  
    
    # Outer loop: iterate through each position in the array
    for i in range(n):  
        # Assume the current position `i` holds the smallest element
        min = i  
        
        # Inner loop: iterate through the unsorted portion of the array
        for j in range(i + 1, n):  
            # If a smaller element is found, update `min` to its index
            if array[j] < array[min]:  
                min = j  
        
        # Swap the current element at index `i` with the smallest element found
        array[i], array[min] = array[min], array[i]  
    
    # Return the sorted array
    return array  

# Input array to be sorted
array = [60, 50, 95, 80, 70]

# Print the result of sorting the input array
print(selectionSort(array))
