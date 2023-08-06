
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, arr
    mid = len(arr) // 2
    left, left_duplicates = merge_sort(arr[:mid])
    right, right_duplicates = merge_sort(arr[mid:])
    merged, duplicates = merge(left, right)

    duplicates.update(left_duplicates)
    duplicates.update(right_duplicates)

    return merged, duplicates

def merge(left, right):
    merged = []
    duplicates = set()

    i = j = 0
    while i < len(left) and  j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            merged.append(right[i])
            duplicates.add(left[i])
            i += 1
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged , duplicates

arr = [2,2,5,3,3,4,5,5,5,4,3,6,77,89,9]

merged , duplicates = merge_sort(arr)
if len(duplicates) < len(merged):
    print("Duplicates present")

    
