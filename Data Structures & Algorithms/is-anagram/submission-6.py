class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet1 = defaultdict(int)
        alphabet2 = defaultdict(int)
        for letter in s:
            alphabet1[letter] +=1
        for letter in t:
            alphabet2[letter] += 1

        return alphabet1 == alphabet2