# 2. Find the Frequency of Each Element in an Array
#    - Problem: Find the No of times the element is present in Array A

class Solution:
    def frequencyCount(self, nums):
        frequency = {}
        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
        return frequency

if __name__ == '__main__':
    nums = [1, 2, 2, 3, 2, 4, 2]
    print(Solution().frequencyCount(nums))