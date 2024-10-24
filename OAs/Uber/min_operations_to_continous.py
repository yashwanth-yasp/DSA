def min_operations_to_continuous(arr):
    # Sort the array to apply the sliding window approach
    arr.sort()
    n = len(arr)
    max_len = 0
    left = 0

    # Use a sliding window to find the longest continuous subarray
    for right in range(n):
        # Ensure no duplicates in the subarray
        while left < right and arr[right] - arr[left] >= n:
            left += 1
        # Update max_len if current subarray is valid and longer
        max_len = max(max_len, right - left + 1)

    # The minimum number of operations needed
    return n - max_len

# Test the function with the given example
#arr = [6, 4, 1, 7, 10]
#arr = [25]
#arr = [25,24]
arr = [2,5,4]
print(min_operations_to_continuous(arr))  # Output: 2
