class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            print(l, r, (r-l)//2, m)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1

        return -1

        # l = 0, r = 5
        # m = 2 != target
        # l = 3, r = 5
        # 5-3 = 2//2 = 1 + 3 = 4 == target