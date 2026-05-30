class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = defaultdict(list)
        result = []
        for s in strs:
            sorted_string = sorted(s)
            sorted_strings["".join(sorted_string)].append(s)

        for l in sorted_strings.values():
            result.append(l)

        return result