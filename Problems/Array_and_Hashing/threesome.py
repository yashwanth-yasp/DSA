
def threesome(arr, k):
    
    result = []
    n = len(arr)

    for i in range(n-2):
        #skipping duplicates
        if i > 0 and arr[i] == arr[i+1]:
            continue

        left, right = i-1 , n-1 

        while left < right:
            curr_sum = arr[left] + arr[right] + arr[i]
            if curr_sum == k:
                result.append([arr[left], arr[i], arr[right]])
                #skipping duplicates
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right += 1
            elif curr_sum > k:
                right -= 1
            else:
                left += 1
    return result

def main():
    arr = [1, 4, 2, 10, 3, 0, 20]
    arr = sorted(arr)
    print(arr)
    k = 8
    result = threesome(arr, k)
    print(result)

main()
