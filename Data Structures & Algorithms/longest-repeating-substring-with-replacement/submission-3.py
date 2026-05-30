class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_characters = {}
        l = 0
        r = 1
        max_characters = 0

        def get_differences_needed(arr, char):
            frequency_dict = {char: 0}
            print(arr)
            for letter in arr:
                if letter == char:
                    frequency_dict[str(letter)] += 1
            return len(arr) - frequency_dict[char]

        for char in s:
            if char not in unique_characters:
                unique_characters[char] = 1

        for UC in unique_characters:
            while r <= len(s):
                if get_differences_needed(s[l:r], UC) <= k:
                    max_characters = max(max_characters, r - l)
                    r += 1
                else:
                    l += 1
                    if l == r:
                        r += 1
            l = 0
            r = 1
                

        return max_characters