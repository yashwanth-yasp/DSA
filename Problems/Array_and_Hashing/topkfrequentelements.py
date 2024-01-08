
def topKFrequent(nums, k):
    freqdict = {}
    for i in nums:
        if i in freqdict.keys():
            freqdict[i] += 1
        else:
            freqdict[i] = 1
    print(freqdict)
    line = sorted(freqdict.items(), key=lambda x:x[1] ,reverse=True)
    result = []
    print(line)
    for i in line:
        result.append(i[0])
    print(result)
    print(result[:k])
    return result[:k]

topKFrequent([1,1,1,2,2,3],2)

