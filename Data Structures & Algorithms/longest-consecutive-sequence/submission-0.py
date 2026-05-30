class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = {}
        max_length = 0

        for num in nums:
            hash_set[num] = 0

        for num in nums:
            length = 0
            if num-1 not in hash_set:
                while num in hash_set:
                    length += 1
                    num += 1
            max_length = max(length, max_length)

        return max_length