def selectionSort(array):
    n = len(array)
    for i in range(n):
        # Assume the first element is the minimum
        min_index = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]
        
    return array

array = [64, 34, 25, 12, 22, 11, 90]
print(selectionSort(array))
