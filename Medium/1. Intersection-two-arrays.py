# Find Intersection of Two Arrays
# Given two arrays, write a function that returns an array of elements found in both arrays (intersection).

# Example Input: arr1 = [1, 2, 3, 4], arr2 = [3, 4, 5, 6]
# Example Output: [3, 4]

def intersectionOfArrays(arr1, arr2):
    arr3 =[]
    for i in arr1:
        if i in arr2:
            arr3.append(i)
    return arr3

def intersectionOfArrays_2(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(intersectionOfArrays(arr1, arr2))
print(intersectionOfArrays_2(arr1, arr2))