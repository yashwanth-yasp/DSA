def Insertion_sort(arr):
    for j in range(1, len(arr)):
        i = j - 1
        key = arr[j]
        while arr[i] > key and i > 0:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr

def main():
    line = [1,2,-99, 0 , 78 , -999, 34, -32 , -30, -11, 345 , 234, 678]
    print(Insertion_sort(line))

if __name__ == '__main__':
    main()