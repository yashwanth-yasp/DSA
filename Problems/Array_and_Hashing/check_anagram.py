
class Solution(object):
    def isAnagram(self, s, t):
        sr = sorted(list(s))
        tr = sorted(list(t))
        if sr != tr:
            return False
        return True
