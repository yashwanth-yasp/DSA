def minWindow(s: str, t: str) -> str:
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

    while end < m:
        if not any(list(freq.values())):
            min_len = min(min_len, end - start)
            min_index = (start, end)
            break
        if moveEnd:
            if freq.get(s[end]):
                freq[s[end]] -= 1
            end += 1
            continue

        if freq.get(s[start]) == None:
            start += 1
        else:
            freq[s[start]] -= 1
            end = start
            moveEnd = True

    print(s[min_index[0] : min_index[1]])
    moveEnd = False

    while end < len(s):
        if moveEnd:
            if not any(list(freq.values())):

                while freq[s[start]] == None:
                    start += 1
    #    freq[start] += 1
    #    start += 1

    #    if freq.get(s[end]):
    #         freq[s[end]] -= 1

    # the end is at one index more than the end marker


s = "axxbxxcxxabc"
t = "abc"
print(s)
print(t)
minWindow(s, t)
