def quickSort(array):
    if len(array) <= 1:
        return array
       
    pivot = array[len(array)//2]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quickSort(left) + middle + quickSort(right)

array = [12, 11, 13, 5, 6]
print(quickSort(array))




