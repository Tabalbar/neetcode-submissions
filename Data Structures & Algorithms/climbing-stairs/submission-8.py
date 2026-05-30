class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i == n:
                return 0
            if i == n-1:
                return 1
            if i == n-2:
                return 2

            if i in cache:
                return cache[i]

            cache[i] = dfs(i + 2) + dfs(i + 1)
            
            return cache[i]
            
        return dfs(0)