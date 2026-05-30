class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]

        forward_pass = 1
        for i, num in enumerate(nums):
            result[i] *= forward_pass
            forward_pass *= num

        backward_pass = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= backward_pass
            backward_pass *= nums[i]

        return result