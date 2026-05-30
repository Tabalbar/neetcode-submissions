class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(1)
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1] 
        running_product = 1
        for i in range(len(nums)-2, -1, -1):
            running_product = nums[i+1] * running_product
            res[i] = res[i] * running_product
        return res