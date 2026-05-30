class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                return True
            else:
                freq_dict[num] = 0

        return False