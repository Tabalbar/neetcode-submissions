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

    def hasSameFrequencyAs(self, sCounter):
        pass

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        t_frequency_counter = FrequencyCounter(t)
        minimum_window = len(s)
        minimum_substr = ""

        while r <= len(s):
            if t_frequency_counter.isWithin(s[l:r]):
                minimum_window = min(len(s[l:r]), minimum_window)
                minimum_substr = s[l:r]

                while t_frequency_counter.isWithin(s[l:r]):
                    minimum_window = min(len(s[l:r]), minimum_window)
                    minimum_substr = s[l:r]
                    r-= 1
                r += 1
                while t_frequency_counter.isWithin(s[l:r]):
                    #shrink left pointer
                    minimum_window = min(len(s[l:r]), minimum_window)
                    minimum_substr = s[l:r]
                    l += 1
                l -= 1
                l += 1
                r += 1
                while r <= len(s):
                    print(s[l:r])
                    if t_frequency_counter.isWithin(s[l:r]):
                        #shrink right pointer
                        while t_frequency_counter.isWithin(s[l:r]):
                            minimum_window = min(len(s[l:r]), minimum_window)
                            minimum_substr = s[l:r]
                            r-= 1
                        r += 1
                        while t_frequency_counter.isWithin(s[l:r]):
                            #shrink left pointer
                            minimum_window = min(len(s[l:r]), minimum_window)
                            minimum_substr = s[l:r]
                            l += 1
                        l -= 1
                        print(s[l:r])
                    l += 1
                    r += 1
                    
            r += 1

        return minimum_substr