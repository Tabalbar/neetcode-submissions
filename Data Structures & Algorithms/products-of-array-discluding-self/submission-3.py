class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        running_prod = nums[0]
        for i in range(len(nums)-1):
            if i == 0:
                res.append(running_prod)
            else:
                running_prod *= nums[i]
                res.append(running_prod)
        running_prod = 1
        for i in range(len(nums)-1, 0, -1):
            running_prod *= nums[i]
            res[i-1] *= running_prod
        return res
# [1,2,4,6]
# [1,1,2,8] #R
# [1,2,4,6]
# [48,24,12,8] #L
