class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        max_len = 0
        for right, letter in enumerate(s):
            while letter in charset:
                charset.remove(s[left])
                left+=1
            charset.add(letter)
            max_len = max(right-left + 1, max_len)
        return max_len

            