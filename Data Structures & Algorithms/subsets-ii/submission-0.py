class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(sorted_nums[i])
            dfs(i + 1)

            subset.pop()
            while i + 1 < len(sorted_nums) and sorted_nums[i] == sorted_nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res