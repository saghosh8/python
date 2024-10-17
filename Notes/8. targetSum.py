def targetSum(array, target):

    left = 0
    right = len(array) -1
    pairs = []

    while left < right:
        if  array[left] + array[right] == target:
            pairs = [array[left] , array[right]]
            left +=1
            right -=1

        elif array[left] + array[right] < target:
            left +=1
       
        else:
            right -=1

    return pairs

array = [1,2,3,4,5]
target = 5
print(targetSum(array,target))