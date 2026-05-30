class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_frequency = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
        
        for letter in t:
            if letter in letter_frequency:
                letter_frequency[letter] -= 1
                if letter_frequency[letter] < 0:
                    del letter_frequency[letter]
            else:
                return False
        print(letter_frequency)
        if 1 in letter_frequency.values():
            return False
        else:
            return True