class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        freq2 = defaultdict(int)
        for letter in s:
            freq[letter] += 1
        for letter in t:
            freq2[letter] += 1
        return freq == freq2
        