class FrequencyCounter:
    def __init__(self, string):
        self.counter = Counter(string)
    
    def isWithin(self, bigger_string):
        bigger_counter = Counter(bigger_string)
        for char in self.counter:
            if char in bigger_counter:
                if bigger_counter[char] < self.counter[char]:
                    return False
            else:
                return False
        return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        t_frequency_counter = FrequencyCounter(t)
        minimum_window = len(s) + 1
        minimum_substr = ""

        while r <= len(s):
            if t_frequency_counter.isWithin(s[l:r]):
                # Try to shrink from both ends while valid
                while t_frequency_counter.isWithin(s[l:r]):
                    if r - l < minimum_window:
                        minimum_window = r - l
                        minimum_substr = s[l:r]
                    l += 1
                l -= 1  # Step back to last valid
            r += 1

        return minimum_substr