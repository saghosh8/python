from typing import List  # Import List from the typing module

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return(seen[diff], i)
            else:
                seen[nums[i]] = i 

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))