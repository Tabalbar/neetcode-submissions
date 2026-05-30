class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        l, r = 0, 0
        frequency_dict = {}

        if len(s) == 1:
            return 1

        while r < len(s):
            while s[r] in frequency_dict:
                del frequency_dict[s[l]]
                l += 1
            frequency_dict[s[r]] = 1
            r += 1
            max_substring_length = max(max_substring_length, len(s[l:r]))
        return max_substring_length