class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_word = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_to_word[sorted_word].append(word)
        return list(anagram_to_word.values())
