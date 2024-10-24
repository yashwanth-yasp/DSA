
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    return binary_search_recursive(arr, low, mid-1, target)

arr = [ 11, 22, 23 ,34, 45 , 56, 67, 98]
print(binary_search_recursive(arr,0, 7, 56))