# 6. Sort Array in increasing Order of their frequency

def freq_sorted(nums):

    # Take an Empty dict
    frequency = {}
    # Iterate through the List
    for i in nums:
    # If element in the frequency dict then increment by 1
        frequency[i] = frequency.get(i, 0) + 1    # If element in the frequency dict then set value as 1
    sorted_frequency = sorted(frequency, key=frequency.get)
    return sorted_frequency

nums = [3, 8, 5, 3, 9, 5, 9, 8, 9, 2, 8, 8]
print(freq_sorted(nums))