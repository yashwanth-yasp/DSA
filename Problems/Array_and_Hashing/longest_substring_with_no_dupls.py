
def lengthOfLongestSubstring( s: str) -> int:
        if not s:
            return 0
        
        left  = 0
        max_len = 0
        window = set()

        for right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                for i in range(right):
                    window.remove(s[i])
                    if s[i] == s[right]:
                        left = i + 1
                        break
            
        
        return max_len

def main():
    arr = "abcabcbb"
    print(arr)
    result = lengthOfLongestSubstring(arr)
    print(result)

main()