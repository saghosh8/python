def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1  # Move to the right half
        else:
            right = mid - 1  # Move to the left half

    return -1  # Target not found

# Example usage:
arr = [10, 20, 30, 40, 50]
target = int(input("Enter the target = "))
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")
