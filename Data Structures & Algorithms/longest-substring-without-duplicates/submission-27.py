from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        q = deque()
        longest_substring = ""
        for i in range(len(s)):
            while s[i] in q:
                q.popleft()
            q.append(s[i])
            if len(q) > len(longest_substring):
                longest_substring = "".join(q)
        return len(longest_substring)
