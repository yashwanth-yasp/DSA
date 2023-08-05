
def sliding_window_variable_size(arr, k):
    if not arr or sum(arr) < k:
        return 0
    
    left, right = 0, 0
    curr_sum = 0
    min_len = len(arr) + 1

    while right < len(arr):

        curr_sum += arr[right]
        while curr_sum >= k:
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1
        
        right += 1
    
    return min_len if min_len <= len(arr) else 0

def main():
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 21
    result = sliding_window_variable_size(arr, k)
    print(result)

main()