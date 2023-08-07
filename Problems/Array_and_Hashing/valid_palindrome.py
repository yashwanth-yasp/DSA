
def isPalindrome( s: str) -> bool:
        if not s:
            return False
        new_str = ""
        for i in s:
            if i.isalnum():
                if i.isalpha() and i.isupper():
                    new_str += i.lower()
                else:
                    new_str += i
        
        left = 0
        right = len(new_str) - 1
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            right -= 1
            left += 1
        return True  

def main():
     s = "racecar"
     print(isPalindrome(s))
            
main()