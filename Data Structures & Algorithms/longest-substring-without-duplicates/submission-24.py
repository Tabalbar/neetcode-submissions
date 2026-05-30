class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        l, r = 0, 1

        if len(s) == 1:
            return 1
        
        def contains_duplicates(arr):
            frequency_dict = {}
            for char in arr:
                if char in frequency_dict:
                    return True
                else:
                    frequency_dict[char] = 1
            return False

        while r < len(s):
            if contains_duplicates(s[l:r]):
                l += 1
            else:
                max_substring_length = max(max_substring_length, len(s[l:r]))
                r += 1
        if not contains_duplicates(s[l:r]):
            max_substring_length = max(max_substring_length, len(s[l:r]))
        return max_substring_length