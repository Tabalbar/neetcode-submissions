class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for num in nums]
        running_prod = 1
        # [1,2,4,6]
        # [1,1,1,1]

        # [1,1,2,8]
        # [48,24,12,8]
        for i in range(1, len(nums)):
            running_prod = nums[i-1] * running_prod
            res[i] *= running_prod
        running_prod = 1
        for i in range(len(nums)-2, -1, -1):
            running_prod = nums[i+1] * running_prod
            res[i] *= running_prod

        return res