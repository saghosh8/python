def linearSearch(array, target):
    for index in range(len(array)):
        if (array[index] == target) :
            return index
    return -1

array = [4, 2, 3, 1]
target = 3
print(linearSearch(array, target))