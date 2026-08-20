class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        result = []
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in freq:
                freq[sorted_s].append(s)
            else:
                freq[sorted_s] = [s]

        for key in freq:
            result.append(freq[key])
        return result