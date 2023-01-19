
def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j+ 1] = arr[j + 1] , arr[j]
    return arr
    
def main():
    line = [1,2,-99, 0 , 78 , -999, 34, -32 , -30, -11, 345 , 234, 678]
    print(Bubble_Sort(line))

if __name__ == '__main__':
    main()