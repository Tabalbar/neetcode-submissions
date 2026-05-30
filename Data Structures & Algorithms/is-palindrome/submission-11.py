class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s)-1
        s = s.lower()
        while pointer1 <= pointer2:
            char1 = s[pointer1]
            char2 = s[pointer2]
            if char1 == " " or not char1.isalnum():
                pointer1+=1
            elif char2 == " " or not char2.isalnum():
                pointer2-=1
            else:
                if char1 != char2:
                    return False
                pointer1+=1
                pointer2-=1
        return True