
def kadanes_algo(arr):
    curr_sum = 0
    max_sum = arr[0]

    for i in arr:
        curr_sum = max(curr_sum, 0) + i
        max_sum = max(curr_sum, max_sum)
    
    return max_sum


line = list(map(int, input().split()))
print(f"The max sum is {kadanes_algo(line)}")



