class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        l = 0
        r = len(nums)-1
        m = 1
        # [-1,0,1,2,-1,-4]
        # [0,1,1]

        # [-4,-1L,-1M,0,1,2R]
        # -3


        # [-1L, 0M 1R,]
        # [-1,0,1,2,-1,-4,-2,-3,3,0,4]
        # [-4,-3L,-2,-1,-1,0,0,1,2, 3R]
        while l+1 < r:
            m = l + 1
            while m < r:
                total = nums[l] + nums[r] + nums[m]
                if total == 0:
                    res.add((nums[l], nums[r], nums[m]))
                    m += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    m += 1
            l += 1
            r = len(nums)-1

        return [list(x) for x in res]