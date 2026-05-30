class Solution:
    def climbStairs(self, n: int) -> int:
        num_distinct_ways_to_climb = 0
        memo = {}

        def dfs(i: int) -> None:
            if i == n:
                return 0
            elif i == n-1:
                return 1
            elif i == n-2:
                return 2
            if i in memo:
                return memo[i]
            else:
                memo[i] = dfs(i + 1) + dfs(i + 2)

                return memo[i]

        num_distinct_ways_to_climb = dfs(0)
        return num_distinct_ways_to_climb
