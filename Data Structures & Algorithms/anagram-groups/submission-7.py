from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outer_list = defaultdict(list)
        result = []
        for s in strs:
            sorted_string = sorted(s)
            freq = Counter("".join(sorted_string))
            outer_list[str(freq)].append(s)
        for s in outer_list.values():
            result.append(s)
        return result

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         outer_list = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             outer_list[tuple(count)].append(s)
#         return list(outer_list.values())