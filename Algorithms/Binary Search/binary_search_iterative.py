
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        print(mid)
        if arr[mid] == target:
            print("found")
            return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [ 11, 22, 23 ,34, 45 , 56, 67, 98]
print(binary_search(arr,3))