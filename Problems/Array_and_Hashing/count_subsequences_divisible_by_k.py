
def count_subsequences(arr, k):
    big_arr = [[] for _ in range(len(arr))]
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            temp = arr[i] + arr[j]
            if temp % k == 0:
                big_arr[i].append(j)
                res += 1 
    total = 0
    for i in big_arr:
        total = recursion_func(big_arr, i, total)
    
    total = total + res

    print(big_arr)
    print(total)

def recursion_func(biggerarr, big_arr, total):
    if len(big_arr) == 0:
        return total 
    for i in big_arr:
        total += 1
        recursion_func(biggerarr, biggerarr[i], total)
        return total   
    return total 

A = [2,4,4,5,6,6]
K = 3
count_subsequences(A, K)


