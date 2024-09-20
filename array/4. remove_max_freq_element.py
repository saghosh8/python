# 4. Remove the numsay element with MAX Freqquency
#    - Problem: Remove the element with MAX Frequency
#    - WithOut pop

class Solution:
    def find_freq(self, nums):
        frequency = {}
        
        # Count frequency of each element
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        return frequency

    def remove_max_freq_element(self, nums):
        frequency = self.find_freq(nums)
        
        # Get the maximum frequency
        max_freq = max(frequency.values())
        
        # Find the elements with maximum frequency
        max_freq_elements = [num for num, freq in frequency.items() if freq == max_freq]

        # Create a new list excluding elements with maximum frequency
        nums = [num for num in nums if num not in max_freq_elements]
        
        return nums

if __name__ == '__main__':          
    nums = [1, 2, 3, 4, 5, 6, 1, 2, 2]
    print(Solution().remove_max_freq_element(nums))
