# 5. Remove all the occurence of duplicate array


def remove_duplicate(nums):
    set_nums = []
    for i in nums:
        if i not in set_nums:
            set_nums.append(i)
    return set_nums


nums = [3, 8, 5, 3, 9, 1, 5, 7, 9, 2, 8]
print(remove_duplicate(nums))
