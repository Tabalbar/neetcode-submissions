class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(step):
            if step == n or step == n-1:
                return 1

            return (dfs(step + 1))+ (dfs(step + 2))

        return dfs(0)