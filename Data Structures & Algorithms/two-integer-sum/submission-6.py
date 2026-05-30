class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for idx, num in enumerate(nums):
            if num not in complement:
                complement[target - num] = idx
            else:
                return [complement[num],idx]
        
