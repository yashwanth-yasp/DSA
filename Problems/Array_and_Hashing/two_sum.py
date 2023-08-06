
def two_sum(arr, k):
    left, right = 0 , len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == k:
            return left, right
        elif sum > k:
            right -= 1
        else:
            left += 1
    
    return 0

def main():
    arr = [1, 4, 2, 10, 3, 0, 20]
    arr = sorted(arr)
    print(arr)
    k = 12
    result = two_sum(arr, k)
    print(result)

main()