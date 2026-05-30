class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_frequency = {}

        for num in nums:
            if num in number_frequency:
                return True
            else:
                number_frequency[num] = 1

        return False