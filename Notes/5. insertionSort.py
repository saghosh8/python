def selectionSort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = key
    return array

array = [64, 34, 25, 12, 22, 11, 90]
print(selectionSort(array))