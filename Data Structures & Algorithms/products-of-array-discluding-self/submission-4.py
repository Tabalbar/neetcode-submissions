class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        running_prod = 1
        for idx in range(len(nums)-1):
            running_prod *= nums[idx]
            res[idx + 1] *= running_prod

        running_prod = 1
        for idx in range(len(nums)-1, 0, -1):
            running_prod *= nums[idx]
            res[idx - 1] *= running_prod

        return res