from collections import Counter

def longest_palindrome(s: str) -> str:
    freq = Counter(s)
    left_half = []
    middle = None
    
    
    for char in sorted(freq.keys()):
        count = freq[char]
        if count % 2 == 0:
            left_half.append(char * (count // 2))
        else:
            if not middle:
                middle = char
            left_half.append(char * (count // 2))
    

    left_half_str = ''.join(left_half)

    right_half_str = left_half_str[::-1]
    
    if middle:
        return left_half_str + middle + right_half_str
    else:
        return left_half_str + right_half_str

s = "aaabb"
print(longest_palindrome(s))  
