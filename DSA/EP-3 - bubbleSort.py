def bubbleSort(array):
    n = len(array)
    # Outer loop to traverse through all elements
    for i in range(n):
        # Track if any swaps happen in this iteration
        swapped = False
        # Inner loop for comparison within the unsorted part of the array
        for j in range(n-1-i):
            # Compare adjacent elements
            if array[j] > array[j+1]:  
                # Swap if elements are in the wrong order
                array[j], array[j+1] = array[j+1], array[j]
                # Mark that a swap has occurred
                swapped = True  
        # If no swaps, array is sorted       
        if not swapped:  
            break
    # Return the sorted array   
    return array  # Return the sorted array

array = [60, 50, 95, 80, 70]
print(bubbleSort(array))