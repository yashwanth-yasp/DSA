
def encode(strs):
    res = ''
    for i in strs:
        encoded = str(len(i)) + '/' + i
        res += encoded
    print(res)
    return res

def decode(str):
    res = []
    i = 0
    while i < len(str):
        e = i
        while e < len(str) and str[e] != '/':
            e += 1
        size = int(str[i:e])
        word = str[e+1, e+1+size]
        res.append(word)
        
    return res