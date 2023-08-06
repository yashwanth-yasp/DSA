
def selection_sort(arr):
    for i in range(len(arr) -1):
        min_index = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index] , arr[i]
    return arr

def main():
    line = [1,2,-99, 0 , 78 , -999, 34, -32 , -30, -11, 345 , 234, 678]
    print(selection_sort(line))

if __name__ == '__main__':
    main()