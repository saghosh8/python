# 3. Remove the array element 
#    - Problem: Remove the element Present in immediately to the right of the element entered by the User

class Solutions:
    def remove_element(self, nums, Element):
        removedElementArray = []
        i = 0
        while i < len(nums):
            if nums[i] == Element:
                removedElementArray.append(nums[i])
                i += 2
            else:
                removedElementArray.append(nums[i])
                i += 1
        return removedElementArray


if __name__ == '__main__':
    nums= [1, 4, 5, 6, 8, 3]
    Element = int(input('Enter the element: '))
    print(Solutions().remove_element(nums, Element))