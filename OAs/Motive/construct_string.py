
def construct_string(arr):
    max_len = max(len(word) for word in arr)
    
    result = []
    for i in range(max_len):
        for word in arr:
            if i < len(word):
                result.append(word[i])
    return ''.join(result)

arr = ["Daisy", "Rose", "Hyacinith", "Poppy"]
print(construct_string(arr)) 