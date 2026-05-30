class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        substring_dict = {}
        left = 0
        substring = ""
        longest_length = 0
        for i in range(len(s)):
            while s[i] in substring:
                if len(substring) > longest_length:
                    longest_length = len(substring)
                substring_as_list = list(substring)
                letter = substring_as_list.pop(0)
                substring = "".join(substring_as_list)
                print(substring)
            substring += s[i]
        return max(longest_length, len(substring))