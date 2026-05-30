class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        for i in range(len(s2)):
            sorted_substring_s2 = "".join(sorted(s2[i:i+len(sorted_s1)]))
            if sorted_substring_s2 == sorted_s1:
                return True
        return False