class Solution:

    def get_majority_element(self, characters: List[str]) -> str:
        counter = Counter(characters)
        buckets = {i:[] for i in range(len(characters) + 1)}
        for char in counter:
            buckets[counter[char]].append(char)
        for i in range(len(buckets)-1, -1,-1):
            if len(buckets[i]) > 0:
                return buckets[i][0]
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        characters = deque()
        max_difference = 0

        while r < len(s):
            characters.append(s[r])

            max_freq_char = self.get_majority_element(characters)
            count = characters.count(max_freq_char)
            difference = len(characters) - count
            while difference > k:
                characters.popleft()
                max_freq_char = self.get_majority_element(characters)
                characters.count(max_freq_char)
                difference = len(characters) - count
            print(count, max_difference)
            max_difference = max(count+ difference, max_difference )
            r+=1
        return max_difference