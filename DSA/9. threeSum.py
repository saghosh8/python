def threeSum(array):
    array.sort()
    triplets = []

    for i in range (len(array) - 2):
        if i > 0 and array[i] == array[i-1]:
            continue
        
        left = i+1
        right = len(array)-1

        while left<right:
            currentSum = array[i] + array[left] + array[right]

            if currentSum == 0:
                triplets.append((array[i] , array[left] , array[right]))
                left +=1
                right -=1

            elif currentSum < 0:
                left +=1
            else:
                right -=1
    return triplets


array = [-1, 0, 1, 2, -1, -4]
print(threeSum(array))
