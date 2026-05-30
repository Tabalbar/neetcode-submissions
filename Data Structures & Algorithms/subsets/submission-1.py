class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(n):
            if n == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[n])
            dfs(n + 1)

            subset.pop()
            dfs(n + 1)

            

        dfs(0)

        return res

