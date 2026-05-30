class Solution:

    def get_majority_element(self, characters: List[str]) -> str:
        counter = Counter(characters)
        buckets = {i:[] for i in range(len(characters) + 1)}
        for char in counter:
            buckets[counter[char]].append(char)
        for i in range(len(buckets)-1, -1,-1):
            if len(buckets[i]) > 0:
                return i
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        characters = defaultdict(int)
        max_frequency = 0
        max_difference = 0

        while r < len(s):
            characters[s[r]] += 1

            max_frequency = max(max_frequency,  characters[s[r]])
            
            while (r - l + 1) - max_frequency > k:
                characters[s[l]] -= 1
                l += 1

            max_difference = max(r - l + 1, max_difference )
            r+=1
        return max_difference