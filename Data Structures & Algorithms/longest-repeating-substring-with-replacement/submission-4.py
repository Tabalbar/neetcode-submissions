class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        r, l = 0, 0

        max_length = 0
        curr_maxf = 0

        for char in s:
            counts[char] = 0

        while r < len(s):
            counts[s[r]] += 1
            curr_maxf = max(curr_maxf, counts[s[r]])

            
            while (r - l + 1) - curr_maxf > k:
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, (r - l + 1))
            r += 1

        return max_length
            