class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict_s = {}
        freq_dict_t = {}

        for char in s:
            
            if char in freq_dict_s:
                freq_dict_s[char] += 1
            else:
                freq_dict_s[char] = 0

        for char in t:
            
            if char in freq_dict_t:
                freq_dict_t[char] += 1
            else:
                freq_dict_t[char] = 0

        return (freq_dict_t.items() == freq_dict_s.items())