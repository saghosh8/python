from typing import List  # Import List from the typing module


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # Sort the array
        nums3 = nums1 + nums2
        sorted_arr = sorted(nums3)
        n = len(sorted_arr)
        
        # Check if the length of the array is odd or even
        if n % 2 == 1:
            # Odd length, return the middle element
            return sorted_arr[n // 2]
        else:
            # Even length, return the average of the two middle elements
            middle1 = sorted_arr[n // 2 - 1]
            middle2 = sorted_arr[n // 2]
            return (middle1 + middle2) / 2
        
nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))