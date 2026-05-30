
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            anagrams_dict[sorted_string].append(string)
        return list(anagrams_dict.values())