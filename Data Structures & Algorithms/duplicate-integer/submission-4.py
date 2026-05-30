class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_seen_in_array = []

        for num in nums:
            if num in numbers_seen_in_array:
                return True
            else:
                numbers_seen_in_array.append(num)

        return False