class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s)-1
        lower_s = s.lower()
        while pointer1 <= pointer2:
            left = lower_s[pointer1]
            right = lower_s[pointer2]
            if not right.isalnum():
                pointer2 -= 1
            elif not left.isalnum():
                pointer1 += 1
            elif left != right:
                return False
            else:
                pointer1 += 1
                pointer2 -= 1
        return True
 