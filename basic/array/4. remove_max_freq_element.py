# 4. Remove the numsay element with MAX Freqquency
#    - Problem: Remove the element with MAX Frequency
#    - WithOut pop

class Solution:
   
    def removeMaxFreq(self, nums):
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        max_freq_element = max(frequency, key=frequency.get)
        del frequency[max_freq_element]
        return frequency


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 2, 4, 2]
    print(Solution().removeMaxFreq(nums))