class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_frequency = {}
        for letter in s:
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
        
        for letter in t:
            if letter in letter_frequency:
                if letter_frequency[letter] > 0:
                    letter_frequency[letter] -= 1
                else:
                    return False
            else:
                return False
        for key in letter_frequency:
            if letter_frequency[key] > 0:
                return False
        return True