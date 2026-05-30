class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                return True
            else:
                frequency_dict[num] = 1

        return False