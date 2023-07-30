
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(freq)):
            if freq[i] != 0:
                return False
            
        return True