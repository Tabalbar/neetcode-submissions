class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_word = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1
            
            anagram_to_word[tuple(count)].append(word)
        return list(anagram_to_word.values())