def targetSum(array, target):

    left = 0
    right = len(array) -1
    pairs = []

    while left < right:
        current_sum = array[left] + array[right]
        if  current_sum == target:
            #pairs = left , right
            pairs.append((array[left], array[right]))
            
            left +=1
            right -=1

        elif current_sum < target:
            left +=1
       
        else:
            right -=1

    return pairs

array = [1,2,3,4,5]
target = 5
print(targetSum(array,target))