class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_frequency = {}
        for letter in s:
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
        
        for letter in t:
            if letter in letter_frequency:
                letter_frequency[letter] -= 1
            else:
                return False
        
        if 1 in letter_frequency.values():
            return False
        else:
            return True