class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "").lower()
        left = 0
        right = len(new_s)-1
        while left < right:
            if new_s[left].isalnum() and new_s[right].isalnum():
                if new_s[left] == new_s[right]:
                    left+=1 
                    right-=1 
                else:
                    return False
            else:
                if not new_s[left].isalnum():
                    left+=1
                if not new_s[right].isalnum():
                    right-=1
        return True