class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            left = dfs(i + 2)
            right = dfs(i + 3)

            memo[i] = max(nums[i] + left, nums[i] + right)
            
            return memo[i]

        rob1 = dfs(0)
        rob2 = dfs(1)
        return max(rob1, rob2)