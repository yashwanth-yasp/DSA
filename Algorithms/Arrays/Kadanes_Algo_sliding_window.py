
def Kadane_sliding_win(arr):
    curr_sum = 0
    max_sum = arr[0]
    max_l , max_r = 0 , 0
    L = 0
    R = 0

    for R in range(len(arr)):
        if curr_sum < 0:
            curr_sum = 0
            L = R
        
        curr_sum += arr[R]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_l, max_r = L , R

    return [max_l, max_r]

