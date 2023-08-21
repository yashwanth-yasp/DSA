
def minWindow(s:str, t:str) -> str:
    start = 0
    end = 0
    freq = {}
    m = len(s)
    for i in t:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    moveEnd = False
    min_index = (start, end)
    min_len = len(s) + 1