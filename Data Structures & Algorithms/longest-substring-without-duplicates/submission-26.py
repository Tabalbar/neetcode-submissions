class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_substring = 0
        char_set = set()
        while r < len(s):
            char_set.add(s[r]) 
            length = len(char_set) 
            longest_substring = max(length, longest_substring)
                     

            r+=1
            while l < r and r < len(s) and s[r] in char_set:
                char_set.discard(s[l])
                l += 1 
        return longest_substring