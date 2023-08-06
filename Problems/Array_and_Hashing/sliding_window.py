
def sliding(arr, k):
    if not arr or k < 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i-k]
        max_sum = max(window_sum , max_sum)
    
    return max_sum , i - k + 1 , i 

def main():
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 3
    result = sliding(arr, k)
    print(result)

main()