class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        running_sum = 0
        max_sum = float("-inf")
        while r < len(nums):
            
            
            if running_sum < 0:
                l = r
                running_sum = 0
            running_sum += nums[r]
            r += 1

            max_sum = max(max_sum, running_sum)

        return max_sum